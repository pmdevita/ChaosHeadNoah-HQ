from pathlib import Path
import os

p = Path(r"C:\Users\pmdevita\AppData\Roaming\yuzu\dump\0100C17017CBC000\romfs\movie")

for root, folders, files in os.walk(p):
    for file in files:
        print(file)
    break

