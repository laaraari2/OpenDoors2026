
import os
import re

filepath = r'c:\Users\laara\OneDrive\Desktop\ALOUMRANE\الأبواب المفتوحة\open_doors_technical_card.html'
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    encoding = 'utf-8'
except UnicodeDecodeError:
    with open(filepath, 'r', encoding='windows-1256') as f:
        content = f.read()
    encoding = 'windows-1256'

# We want to find the animateurs table and update its rows.
# The table starts after <h2>لائحة منشطي الورشات</h2>
# Each row in the tbody has 4 cells. The 3rd cell is Requirements.

def process_row(match):
    prefix = match.group(1)
    requirements = match.group(2)
    suffix = match.group(3)
    
    # Only update if requirements is empty or whitespace
    if not requirements.strip():
        new_requirements = "قبعة (Casquette) تحمل شعار المؤسسة + شارة (Badge)"
        return f"{prefix}{new_requirements}{suffix}"
    else:
        # If not empty, maybe append? User said "اضف" (Add).
        # Let's append if it doesn't already contain it.
        if "قبعة" not in requirements:
            new_requirements = requirements.strip() + " + قبعة (Casquette) تحمل شعار المؤسسة + شارة (Badge)"
            return f"{prefix}{new_requirements}{suffix}"
        return match.group(0)

# Regex to match rows in the animateurs table.
# We look for <tr> followed by two <td>s, then the 3rd <td> we want to edit.
# This is tricky because there are other tables.
# Let's focus on the section between "لائحة منشطي الورشات" and the end of the table.

start_tag = "لائحة منشطي الورشات"
table_start = content.find(start_tag)
tbody_start = content.find("<tbody>", table_start)
tbody_end = content.find("</tbody>", tbody_start)

table_body = content[tbody_start:tbody_end]

# Match the 3rd <td> in each <tr>
# Pattern: <tr> ... <td>...</td> <td>...</td> <td>(HERE)</td> ... </tr>
row_pattern = re.compile(r'(<tr>\s*<td>.*?</td>\s*<td>.*?</td>\s*<td>)(.*?)(</td>)', re.DOTALL)

new_table_body = row_pattern.sub(process_row, table_body)

new_content = content[:tbody_start] + new_table_body + content[tbody_end:]

with open(filepath, 'w', encoding=encoding) as f:
    f.write(new_content)

print("Requirements updated for all animateurs.")
