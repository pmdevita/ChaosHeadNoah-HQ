from ffmpeg import ffmpeg
from utils import convert_timestamp_to_ffmpeg, relative_crop
from pathlib import Path
from asset_paths import xbox_mv2, switch_mv, project_base

videos = [xbox_mv2 / "dx_01.mkv", switch_mv / "mvinter01.webm",
          project_base / "scripts/vapoursynth/VSGAN-tensorrt-docker/test.mkv"]
output = Path("../comparisons/upscale_compare4.png")
# Hours:Minutes:Seconds
ts = "00:00:2"
frame = 17

for i, vid in enumerate(videos):
    out_path = output.with_stem(output.stem + "_" + str(i))
    ffmpeg(vid, ["-y", "-ss", convert_timestamp_to_ffmpeg(vid, ts, frame), "-frames:v", "1",
               "-vf", f"crop={relative_crop(vid, (1280, 720), (100, 100), (400, 400))}"], out_path, debug=True)

