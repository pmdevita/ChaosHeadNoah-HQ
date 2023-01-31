from ffmpeg import ffprobe
from pathlib import Path


def zero_pad(num, pad):
    n = str(num)
    return "".join(["0" for i in range(pad-len(n))]) + n


def find_video_stream(data):
    # Find the video stream
    vid_stream = 0
    if "streams" not in data:
        return None
    while data["streams"][vid_stream]["codec_type"] != "video":
        vid_stream += 1
    return data["streams"][vid_stream]


def convert_timestamp_to_ffmpeg(video_path: Path, time, frame):
    """Takes a string timestamp hour:minute:second and a frame number and returns a string for ffmpeg -ss"""
    # Convert frame number to milliseconds
    data = ffprobe(video_path, debug=True)
    vid = find_video_stream(data)
    # Convert ratio to 2-tuple of ints
    frame_rate_ratio = [int(i) for i in vid["r_frame_rate"].split("/")]
    frame_rate = frame_rate_ratio[0] / frame_rate_ratio[1]
    millisecond = round(1 / frame_rate * frame, 5)
    return time + str(millisecond)[1:]


def relative_crop(vid: Path, original_dimensions: tuple, coordinates: tuple, size: tuple):
    """

    :param vid: Path to new video to adapt crop to
    :param original_dimensions: Dimensions of the original image this crop was made for as 2-tuple (w, h)
    :param coordinates: Top-left coordinate of the crop box as 2-tuple (x, y)
    :param size: Size of the crop box as 2-tuple (w, h)
    :return: String to use for cropping in ffmpeg
    """
    data = find_video_stream(ffprobe(vid))
    new_dims = (data["width"], data["height"])
    new_coords = (coordinates[0] / original_dimensions[0] * new_dims[0],
                  coordinates[1] / original_dimensions[1] * new_dims[1])
    new_size = (size[0] / original_dimensions[0] * new_dims[0],
                size[1] / original_dimensions[1] * new_dims[1])
    return f"{new_size[0]}:{new_size[1]}:{new_coords[0]}:{new_coords[1]}"



