import subprocess
import os
from pathlib import Path
from ffmpeg import ffmpeg

p = Path(r"D:\SteamLibrary\steamapps\common\CHAOS;HEAD NOAH\Data\movie_eng")

# The CRID USM extractor (video demultiplexer) in VGMToolbox adds this extra number on the filenames, ID0000_XXXXXXX.ext
vid_number = 40534656
aud_number = 40534641

for root, folders, files in os.walk(p):
    r = Path(root)
    for file in files:
        f = r / file
        if f.suffix == "":
            ffmpeg([r / f"{file}_{vid_number}.m2v", "-i", r / f"{file}_{aud_number}.hca"],
                   ["-y", "-c:v", "h264_nvenc", "-crf", "10", "-c:a", "flac"],
                   r / f"{file}.mkv")
