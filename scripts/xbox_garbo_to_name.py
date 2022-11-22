import os
import json
from utils import zero_pad
from asset_paths import xbox_bgm, xbox_base

# This replaces the corrupted file names from the afs
# archive extractor with just numerical names by using the
# JSON manifest it exports

p = xbox_bgm
manifest = xbox_base / "bgm.json"
name = "bgm"
extension = "adx"

with open(manifest) as f:
    m = json.load(f)

for i, entry in enumerate(m["Entries"]):
    filename = p / entry["FileName"]
    os.rename(filename, p / f"{name}_{zero_pad(i, 2)}.{extension}")

