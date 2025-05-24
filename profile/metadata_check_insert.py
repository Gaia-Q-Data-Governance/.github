"""
Check or insert YAML metadata in markdown files.
Usage:
    python metadata_check_insert.py file1.md [file2.md ...]
"""

import sys
import pathlib
from datetime import date

YAML_TEMPLATE = """---
title: [Document Title]
version: 1.0
date: {today}
authors: [Your Name, Team]
reviewers: [Reviewer Name, Board]
infoCode: [DOC-CODE]
status: DRAFT
extensions: []
---
"""

def has_yaml_metadata(text):
    return text.lstrip().startswith("---")

def insert_metadata(fname):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    if has_yaml_metadata(content):
        print(f"{fname}: Metadata already present.")
        return
    metadata = YAML_TEMPLATE.format(today=date.today())
    with open(fname, "w", encoding="utf-8") as f:
        f.write(metadata + "\n" + content)
    print(f"{fname}: Metadata inserted.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python metadata_check_insert.py file1.md [file2.md ...]")
        sys.exit(1)
    for fname in sys.argv[1:]:
        insert_metadata(fname)