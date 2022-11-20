import os
from pathlib import Path
import json
from utils import zero_pad

p = Path(r"D:\Users\pmdevita\Downloads\Chaos;Head Noah\dx2")
manifest = Path(r"D:\Users\pmdevita\Downloads\Chaos;Head Noah\dx2.json")

with open(manifest) as f:
    m = json.load(f)

for i, entry in enumerate(m["Entries"]):
    print(i)
    filename = p / entry["FileName"]
    os.rename(filename, p / f"dx_{zero_pad(i, 2)}.ngs")

