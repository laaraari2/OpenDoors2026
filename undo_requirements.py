
import os

filepath = r'c:\Users\laara\OneDrive\Desktop\ALOUMRANE\الأبواب المفتوحة\open_doors_technical_card.html'
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    encoding = 'utf-8'
except UnicodeDecodeError:
    with open(filepath, 'r', encoding='windows-1256') as f:
        content = f.read()
    encoding = 'windows-1256'

# Remove the added text
added_text = "قبعة (Casquette) تحمل شعار المؤسسة + شارة (Badge)"
# Note: My script might have added " + " if there was existing text.
# But in our case they were mostly empty.
new_content = content.replace(added_text, "")

with open(filepath, 'w', encoding=encoding) as f:
    f.write(new_content)

print("Animateurs table cleaned.")
