from pathlib import Path
import os
from asset_paths import xbox_bg

p = xbox_bg


def get_file_listing(path: Path):
    for root, folders, files in os.walk(path):
        return sorted(files)


if __name__ == '__main__':
    for file in get_file_listing(p):
        print(file)

