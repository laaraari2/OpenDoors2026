import subprocess
import sys
try:
    import pdfplumber
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfplumber", "pandas"])
    import pdfplumber
    import pandas as pd

pdf_path = "porteOuverte.pdf"
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table)
            df.to_csv(f"table_page_{i+1}.csv", index=False, encoding="utf-8-sig")
            print(f"Table extracted from page {i+1} and saved to table_page_{i+1}.csv")
