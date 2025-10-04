#!/bin/bash
# unique_ips.sh — выводит все уникальные IP клиентов

grep -Eo 'on [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:' "$1" \
    | awk '{print $2}' \
    | sed 's/:.*//' \
    | sort -u