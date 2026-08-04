import glob
import os

PRD_DIR = "/home/sunil/Dev/Brando/prd"
OUTPUT_FILE = "/home/sunil/Dev/Brando/prdv2.md"

files = sorted(glob.glob(os.path.join(PRD_DIR, "[0-9][0-9]_*.md")))
chunks = []

for fpath in files:
    with open(fpath, encoding="utf-8") as f:
        chunks.append(f.read().strip())

combined = "\n\n---\n\n".join(chunks) + "\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    out.write(combined)

print(f"Successfully synced {len(files)} Funnel PRD tier files into {OUTPUT_FILE}")
