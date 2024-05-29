from pprint import pprint
import re

all_text = {}

with (open('1.txt', 'r', encoding='utf-8') as f1, open('2.txt', 'r', encoding='utf-8') as f2,
      open('3.txt', 'r', encoding='utf-8') as f3, open('4.txt', 'w', encoding='utf-8') as main):
    for file in f1, f2, f3:
        text = file.readlines()
        length = 0
        for line in text:
            length += 1
        all_text[file.name] = (length, text)
        sorted_text = str(sorted(all_text.items(), key=lambda x: x[1]))
    for el in sorted_text:
        a = re.sub(r'[^A-Za-z0-9-А-я.,]', ' ', el)
        a = a.replace('n', '')
        main.write(a)

pprint(repr(sorted_text))

