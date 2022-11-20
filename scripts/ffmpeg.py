from __future__ import annotations
import subprocess
from pathlib import Path
import json


class HardwareDecode:
    DEFAULT = "SOFTWARE"
    SOFTWARE = "SOFTWARE"
    NVIDIA = "NVIDIA"
    FULL_NVIDIA = "FULL_NVIDIA"


def ffmpeg(input_files: Path | list[Path], flags: list, output: Path, decoder=HardwareDecode.DEFAULT, debug=False):
    args = ["ffmpeg", "-hide_banner"]

    if decoder == HardwareDecode.NVIDIA:
        args.extend(["-hwaccel", "cuda"])
    elif decoder == HardwareDecode.FULL_NVIDIA:
        args.extend(["-hwaccel", "cuda", "-hwaccel_output_format", "cuda"])

    if isinstance(input_files, Path):
        input_files = [input_files]
    for file in input_files:
        args.append("-i")
        args.append(str(file))

    args.extend(flags)
    args.append(str(output))
    if debug:
        print(args)
    p = subprocess.Popen(args)
    p.wait()


def ffprobe(input_file: Path, debug=False):
    args = ["ffprobe", "-v", "quiet", "-print_format",  "json", "-show_format", "-show_streams", str(input_file)]
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    output = p.communicate()[0].decode()
    j = json.loads(output)
    if debug:
        print(json.dumps(j, indent=2))
    return j

