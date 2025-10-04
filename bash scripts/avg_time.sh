#!/bin/bash
# avg_time.sh — считает среднее время обработки запроса (ms)

# Достаём все числа после "spent {" до первого двоеточия
grep -oP 'spent\s*{\s*\K[0-9.]+(?=\s*:)' "$1" \
  | awk '{sum += $1; n++} END { if (n > 0) printf "Average processing time (ms): %.4f\n", sum/n; else print "No data"}'
