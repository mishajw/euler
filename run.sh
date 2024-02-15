#!/usr/bin/env bash
for file in p*.py; do
    output=$(python $file)
    echo "$file: $output"
done
