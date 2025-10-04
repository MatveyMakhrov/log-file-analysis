В этой директории собраны bash скрипты, которые решают задачу с анализом файла с логами.

Задача состоит в том, чтобы определить:
* всех клиентов сервиса (ip-адреса)
* самый популярный запрос
* среднее количество слов в запросах
* среднее время обработки запроса
* максимальное время обработки запроса
* среднее количество запросов в секунду

Я написал для каждой задачи отдельный скрипт.

## Описание и выводы

1)  Все клиенты сервиса (IP-адреса)

[Код скрипта](https://github.com/MatveyMakhrov/log-file-analysis/blob/main/bash%20scripts/unique_ips.sh)

Вывод:
```bash
10.200.243.238
10.200.243.75
10.205.6.127
10.205.6.128
10.205.6.129
10.205.6.130
10.205.6.131
10.205.6.132
10.205.6.133
10.205.6.134
133.0.0.1
134.0.0.1
```

2) Самый популярный запрос

[Код скрипта](https://github.com/MatveyMakhrov/log-file-analysis/blob/main/bash%20scripts/top_query.sh)

Вывод:
```bash
71 how to make a sandwich
```

3) Среднее количество слов в запросах

[Код скрипта](https://github.com/MatveyMakhrov/log-file-analysis/blob/main/bash%20scripts/avg_words.sh)

Вывод:
```bash
Average words per query: 2.65
```

4) Среднее время обработки запроса

[Код скрипта](https://github.com/MatveyMakhrov/log-file-analysis/blob/main/bash%20scripts/avg_time.sh)

Вывод:
```bash
Average processing time (ms): 1.0675
```

5) Максимальное время обработки запроса

[Код скрипта](https://github.com/MatveyMakhrov/log-file-analysis/blob/main/bash%20scripts/max_time.sh)

Вывод:
```bash
Max processing time (ms): 45.7856
```

6) Среднее количество запросов в секунду

[Код скрипта](https://github.com/MatveyMakhrov/log-file-analysis/blob/main/bash%20scripts/rps.sh)

Вывод:
```bash
RPS: 1778.83
```

## Запуск

1. Клонируем репозиторий или заходим в папку со скриптами

```bash
git clone https://github.com/MatveyMakhrov/log-file-analysis.git
cd log-file-analysis/"bash scripts"
```

2. Делаем скрипты исполняемыми

```bash
chmod +x *.sh
```

3. Запуск скрипта

```bash
./unique_ips.sh <path_to_log_file>
./top_query.sh <path_to_log_file>
./avg_words.sh <path_to_log_file>
./avg_time.sh <path_to_log_file>
./max_time.sh <path_to_log_file>
./rps.sh <path_to_log_file>
```
