from pathlib import Path
import re
from urllib.parse import unquote_plus
from collections import Counter
from datetime import datetime
import statistics
import sys


# Функция анализирует лог-файл сервиса и извлекает статистику 
# Принимает: путь к файлу лога (строка)
# Возвращает: ничего (печатает статистику в консоль)
def analyze(path):

    # Читаем лог и задаём шаблоны для поиска IP, запросов, параметра q=, времени обработки и дат
    text = Path(path).read_text(encoding='utf-8', errors='ignore')
    lines = text.splitlines()
    ip_re = re.compile(r'on (\d+\.\d+\.\d+\.\d+):\d+')
    on_conn_query_re = re.compile(r'On Conn\{[^\}]+\} new Query\{[^\}]+\} \[[^\]]+\]: (.+)$')
    full_text_q_re = re.compile(r'Query\{[^\}]+\} \[[^\]]+\] full text: (q=[^&\n\r]+)')
    end_spent_re = re.compile(r'spent\s*\{\s*([0-9]*\.?[0-9]+)\s*:')
    timestamp_re = re.compile(r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d+\s+\d\d:\d\d:\d\d')

    # Контейнеры для собранных данных
    ips = set()
    queries = []
    times_ms = []
    timestamps = []

     # Обходим все строки лога
    for ln in lines:
        # --- IP-адреса ---
        for m in ip_re.finditer(ln):
            ips.add(m.group(1))

        # --- Запросы из "full text: q=..." ---
        m2 = full_text_q_re.search(ln)
        if m2:
            qm = re.search(r'q=([^&\s]+)', m2.group(1))
            if qm:
                try:
                    decoded = unquote_plus(qm.group(1))
                except:
                    decoded = qm.group(1)
            queries.append(decoded)
        
        # --- Время обработки ---
        m3 = end_spent_re.search(ln)
        if m3:
            try:
                times_ms.append(float(m3.group(1)))
            except:
                pass
        
        # --- Временные метки ---
        m4 = timestamp_re.search(ln)
        if m4:
            ts = ln[:15]
            try:
                dt = datetime.strptime(f"{ts} 2025", "%b %d %H:%M:%S %Y")
                timestamps.append(dt)
            except:
                pass

    # Подсчёт статистики 
    num_queries = len(queries)
    most_common = Counter(queries).most_common(1)
    words_counts = [len([w for w in re.split(r'\s+', q.strip()) if w]) for q in queries if q.strip()]
    avg_words = statistics.mean(words_counts) if words_counts else 0
    avg_time_ms = statistics.mean(times_ms) if times_ms else 0
    max_time_ms = max(times_ms) if times_ms else 0
    if timestamps:
        span_seconds = (max(timestamps) - min(timestamps)).total_seconds()
        rps = num_queries / span_seconds if span_seconds>0 else num_queries
    else:
        rps = float('nan')

    # Вывод результатов
    print('Unique IPs:', sorted(ips))
    print('Most popular query:', most_common)
    print('Average words per query:', avg_words)
    print('Average processing time (ms):', avg_time_ms)
    print('Max processing time (ms):', max_time_ms)
    print('Average requests per second:', rps)


# Запускаем анализ только если файл выполняется напрямую  
# Обязателен один аргумент: путь к файлу лога
if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyze(sys.argv[1])
    else:
        print("Error: specify the path to the kyle log when entering the script.")
        print("Usage: python analyze_spcd.py <path_to_file>")
        sys.exit(1)