
import os

filepath = r'c:\Users\laara\OneDrive\Desktop\ALOUMRANE\الأبواب المفتوحة\open_doors_technical_card.html'
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    encoding = 'utf-8'
except UnicodeDecodeError:
    with open(filepath, 'r', encoding='windows-1256') as f:
        lines = f.readlines()
    encoding = 'windows-1256'

for i, line in enumerate(lines):
    if 590 <= i+1 <= 630:
        print(f"{i+1}: {repr(line)}")
