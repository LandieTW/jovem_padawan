#!/usr/bin/env python

import sys
import re
import io
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")

regex = sys.argv[1]

count = 0
for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
    count += 1

print(f"\nN-lines: {count}")
print(f"\n"*2)

# run in CMD
# C:\Users\landi\Downloads\github\ds>type somefile.txt | python stdin_stdout.py "[0-9]"

try:
    n_words = int(sys.argv[1])
except:
    sys.stderr.write(f"Erro: {e}\n")
    sys.exit(1)

counter = Counter()

for line in sys.stdin:
    for word in line.strip().split():
        if word:
            counter[word.lower()] += 1

for word, count in counter.most_common(n_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")

# run in CMD
# type somefile2.txt | python stdin_stdout.py 5

