#!/bin/bash
# max_time.sh — считает максимальное время обработки запроса (ms)

grep -oP 'spent\s*{\s*\K[0-9.]+(?=\s*:)' "$1" \
  | awk 'BEGIN {max=0} {if ($1 > max) max=$1} END {if (max>0) printf "Max processing time (ms): %.4f\n", max; else print "No data"}'
