#!/usr/bin/env python3
import os
from datetime import datetime

OUTPUT = "full_export.md"
EXCLUDE = {".git", ".github", "__pycache__"}
EXCLUDE_FILES = {"index.md", OUTPUT, "README.md"}

def walk_md_files(root="."):
    md_paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        # bezpečně ignoruj systémové složky
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE and not d.startswith(".")]
        for fn in filenames:
            if fn.lower().endswith(".md") and fn not in EXCLUDE_FILES and not fn.startswith("."):
                md_paths.append(os.path.relpath(os.path.join(dirpath, fn), root).replace("\\", "/"))
    return sorted(md_paths, key=str.lower)

def read_text(path):
    # bezpečné čtení – nic nepřepisuje, jen načítá
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read().rstrip()

def main():
    files = walk_md_files(".")
    header = [
        "# Dance Master – Full Export",
        "",
        f"_Auto-generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_",
        "",
        f"_Files included: {len(files)}_",
        "",
        "---",
        ""
    ]

    out = header[:]
    for rel in files:
        out.append(f"\n\n---\n\n# {rel}\n")
        out.append(read_text(rel))
    out.append("\n")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"OK: {OUTPUT} generated ({len(files)} notes)")

if __name__ == "__main__":
    main()
