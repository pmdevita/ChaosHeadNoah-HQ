import os
from pathlib import Path
from ffmpeg import ffmpeg
from asset_paths import steam_bgm

p = steam_bgm

# The CRID USM extractor in VGMToolbox adds this extra number on the filenames, ID0000_XXXXXXX.ext
vid_number = 40534656
aud_number = 40534641

for root, folders, files in os.walk(p):
    r = Path(root)
    for file in files:
        f = r / file
        if f.suffix == "":
            ffmpeg(f, ["-y", "-c:a", "flac"], r / f"{file}.flac")
