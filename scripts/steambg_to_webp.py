import os
from pathlib import Path

p = Path(r"D:\SteamLibrary\steamapps\common\CHAOS;HEAD NOAH\Data\bg")

for root, folders, files in os.walk(p):
    r = Path(root)
    for file in files:
        f = r / file
        if f.suffix == "":
            os.rename(f, f.with_suffix(".webp"))

