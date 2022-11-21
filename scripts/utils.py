def zero_pad(num, pad):
    n = str(num)
    return "".join(["0" for i in range(pad-len(n))]) + n


def find_video_stream(data):
    # Find the video stream
    vid_stream = 0
    while data["streams"][vid_stream]["codec_type"] != "video":
        vid_stream += 1
    return data["streams"][vid_stream]


