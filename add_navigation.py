import os
import re

directory = r'c:\Users\laara\OneDrive\Desktop\ALOUMRANE\الأبواب المفتوحة'
files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'index.html' and 'Copie' not in f]

css_to_inject = """
    <!-- Global Navigation System -->
    <style>
        .back-home {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #1a365d;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            z-index: 10000;
            transition: all 0.3s ease;
            font-size: 1.5rem;
            border: 2px solid white;
        }
        .back-home:hover {
            transform: scale(1.1) translateY(-5px);
            background: #d4af37;
        }
        @media print {
            .back-home { display: none !important; }
        }
    </style>
"""

link_to_inject = '<a href="index.html" class="back-home" title="العودة للرئيسية">🏠</a>'

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid double injection
    if 'class="back-home"' in content:
        print(f"Skipping {filename} (already has back button)")
        continue
    
    # Inject CSS before </head>
    if '</head>' in content:
        content = content.replace('</head>', css_to_inject + '\n</head>')
    
    # Inject Link after <body>
    body_match = re.search(r'<body[^>]*>', content, re.IGNORECASE)
    if body_match:
        content = content[:body_match.end()] + '\n    ' + link_to_inject + content[body_match.end():]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
