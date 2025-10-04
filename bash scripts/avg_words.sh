#!/bin/bash
# avg_words.sh — среднее количество слов без Python

grep -oP 'full text: q=\K[^& ]+' "$1" \
    | sed 's/+/ /g' \
    | perl -MURI::Escape -ne 'print uri_unescape($_)' \
    | awk '
        {
            n=split($0, a, /[ \t]+/);  # считаем слова
            total += n;
            count++;
        }
        END {
            if (count > 0) 
                printf "Average words per query: %.2f\n", total/count;
            else
                print "No queries found";
        }'
