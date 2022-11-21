from ffmpeg import ffmpeg, ffprobe
from utils import find_video_stream
from pathlib import Path

p = Path(r"D:\Users\pmdevita\Downloads\Chaos;Head Noah\dx2\dx_01.mkv")
output = Path("../comparisons/mv_4_xbox.png")
ts = "00:02:53"
frame = 14

# Convert frame number to milliseconds
data = ffprobe(p, debug=True)
vid = find_video_stream(data)
# Convert ratio to 2-tuple of ints
frame_rate_ratio = [int(i) for i in vid["r_frame_rate"].split("/")]
frame_rate = frame_rate_ratio[0] / frame_rate_ratio[1]
millisecond = round(1 / frame_rate * frame, 5)
ts = ts + str(millisecond)[1:]

ffmpeg(p, ["-y", "-ss", ts, "-frames:v", "1"], output, debug=True)

