import os
from pathlib import Path
import shutil

p = Path(r"C:\Users\pmdevita\AppData\Roaming\yuzu\dump\0100C17017CBC000\romfs\bg")
cc = Path(r"C:\Users\pmdevita\AppData\Roaming\yuzu\dump\0100C17017CBC000\romfs\bg_cc")

for root, folders, files in os.walk(p):
    r = Path(root)
    for file in files:
        f = r / file
        if file.startswith("bg") and file.count("_") < 2:
            shutil.move(f, cc / file)


