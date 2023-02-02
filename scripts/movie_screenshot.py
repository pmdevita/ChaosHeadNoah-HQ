from ffmpeg import ffmpeg
from utils import convert_timestamp_to_ffmpeg, relative_crop, FFmpegTimestamp
from pathlib import Path
from asset_paths import xbox_mv2, switch_mv, steam_base, assets_base

videos = {
    "Xbox": xbox_mv2 / "dx_01.mkv",
    "Switch": switch_mv / "mvinter01.webm",
    "Steam": steam_base / "movie" / "ID00058.mkv",
    "Upscale": assets_base / "VidOut" / "opening-cs-aud.mkv"
}
crop = {
    "frame_size": (1280, 720),
    "top_left": (0, 0),
    "size": (1280, 720)
}
time_offset = {
    "Xbox": 1,
    "Switch": 1,
    "Steam": 2,
    "Upscale": 0
}

output = Path("../comparisons/movie/inter/kiss.png")
# Hours:Minutes:Seconds
ts = "00:02:11"
frame = 15

for id, vid in videos.items():
    out_path = output.with_stem(output.stem + "_" + str(id))
    timestamp = FFmpegTimestamp(vid, ts, frame)
    timestamp.frame += time_offset.get(id, 0)
    ffmpeg(vid, ["-y", "-ss", str(timestamp), "-frames:v", "1",
               "-vf", f"crop={relative_crop(vid, crop['frame_size'], crop['top_left'], crop['size'])}"], out_path, debug=True)

