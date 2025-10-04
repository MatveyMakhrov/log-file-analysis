#!/bin/bash
# top_query.sh — самый популярный запрос

grep -oP 'full text: q=\K[^& ]+' "$1" \
    | sed 's/+/ /g' \
    | perl -MURI::Escape -ne 'print uri_unescape($_)' \
    | sort \
    | uniq -c \
    | sort -nr \
    | head -n1
