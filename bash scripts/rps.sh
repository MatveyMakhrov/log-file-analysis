#!/bin/bash
# rps.sh — считает среднее число запросов в секунду

timestamps=$(cut -c1-15 "$1" | grep -E '^[A-Z][a-z]{2} [ 0-9][0-9] [0-9]{2}:[0-9]{2}:[0-9]{2}')
first=$(echo "$timestamps" | head -n1)
last=$(echo "$timestamps" | tail -n1)

start=$(date -d "$first 2025" +%s)
end=$(date -d "$last 2025" +%s)

total=$(grep -c 'full text: q=' "$1")
span=$(( end - start ))

if [ "$span" -gt 0 ]; then
  awk -v t="$total" -v s="$span" 'BEGIN { printf "RPS: %.2f\n", t/s }'
else
  echo "RPS: $total"
fi
