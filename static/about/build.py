#!/usr/bin/python
import os
import sys
from pathlib import Path

includes_root = Path("/home/root/public/includes/")

print("""\
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="/static/style.css"/>
    <title>about</title>
  </head>
  <body>
    <div class="container">
""")

with open(includes_root / "header.html") as f:
    print(f.read())

sys.stdout.flush()

os.system("pandoc -f markdown-smart -t html about.md")

print("""\
    </div>
  </body>
</html>
""")
