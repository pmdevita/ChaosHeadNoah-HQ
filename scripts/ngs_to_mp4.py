import os
from pathlib import Path
import json
from utils import zero_pad
from ffmpeg import ffmpeg, HardwareDecode, ffprobe

# Convert the XBOX 360 NGS files and fix the aspect ratio for some of them

p = Path(r"D:\Users\pmdevita\Downloads\Chaos;Head Noah\dx")

for root, folders, files in os.walk(p):
    r = Path(root)
    for file in files:
        f = r / file
        if f.suffix == ".ngs":
            metadata = ffprobe(f)
            # Find the video stream
            vid_stream = 0
            while metadata["streams"][vid_stream]["codec_type"] != "video":
                vid_stream += 1
            vid_stream = metadata["streams"][vid_stream]
            # Does it have the broken SAR/DAR?
            wrong_sar_flag = False
            if vid_stream["sample_aspect_ratio"] == "200:219" and vid_stream["display_aspect_ratio"] == "3200:1971":
                print("hey", f.parts[-1])
                wrong_sar_flag = True

            args = ["-y", "-c:v", "h264_nvenc",
                    "-preset", "slow", "-profile:v", "high", "-b:v", "25M", "-level", "5.1",
                    "-cq", "5"]
            if wrong_sar_flag:
                args.extend(["-vf", "setsar=sar=1/1"])
            args.extend(["-c:a", "flac"])

            ffmpeg(f, args,
                   f.with_suffix(".mkv"), decoder=HardwareDecode.NVIDIA)


