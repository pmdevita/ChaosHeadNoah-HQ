import subprocess
import os
from pathlib import Path
from ffmpeg import ffmpeg

p = Path(r"C:\Users\pmdevita\AppData\Roaming\yuzu\dump\0100C17017CBC000\romfs\chvoice")
vgmstream_binary = Path(r"D:\Users\pmdevita\Downloads\vgmstream-win\test.exe")


def vgmstream(file: Path):
    p = subprocess.Popen([vgmstream_binary, file])
    p.wait()


for root, folders, files in os.walk(p):
    r = Path(root)
    for file in files:
        f = r / file
        if f.suffix == ".opus":
            vgmstream(f)
            ffmpeg(f.with_suffix(".opus.wav"), ["-y", "-c:a", "flac"], f.with_suffix(".flac"))
            os.remove(f.with_suffix(".opus.wav"))


