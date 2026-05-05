import pandas as pd

df = pd.read_csv('table_page_1.csv')
# The columns are 0 to 10
# Col 10: name (in arabic, reverse it or just match)
# Col 9: 10:00
# Col 8: 10:30
# Col 7: 11:00
# Col 6: 11:30
# Col 5: 12:00
# Col 4: 14:00
# Col 3: 14:30
# Col 2: 15:00
# Col 1: 15:30

html_rows = []
for idx, row in df.iterrows():
    name_ar = str(row['10']).strip()
    if name_ar == 'nan' or name_ar == 'تاشرولا': continue
    
    # We will just print the array of classes for each row from 9 down to 1
    classes = []
    for col in range(9, 0, -1):
        val = str(row[str(col)]).strip()
        if val == 'nan': val = ''
        val = val.replace('(A/B)', '').replace('(A)', 'A').replace('(B)', 'B').replace(' ', '')
        classes.append(val)
    
    print(f"{name_ar}: {classes}")
