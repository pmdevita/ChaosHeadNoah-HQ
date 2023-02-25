# Transcoding and Archive Handling Notes

## Extracting Xbox360 files
- iso extractor https://github.com/XboxDev/extract-xiso/releases/tag/build-202204252159
- npa extractor https://github.com/Wilhansen/nipa/releases
- video file type: ngs container holding mpeg1 and adpcm

## Converting Steam Movies
- YACpkTool to extract cpk files
- VGMToolbox to demux usm

## Decoding Switch Audio
- vgmstream can decode Switch audio files

## Encoding Switch Audio
- Custom encoder

## Upscaling

I'm no better than a script kiddy at ML, let me know if I got anything wrong.

For the model, I chose ~~sudo_RealESRGAN2x_Dropout_3.799.042_G.pth~~ LD-Anime_Compact from here https://upscale.wiki/wiki/Model_Database#Anime. 
~~From the samples, this seemed to avoid the overly sharp yet blobby lines that were common in some of the 
other models, or even the larger RealESRGAN_x4plus_anime.~~ Chaos;Head's animation has very soft lines and textures, 
and LD-Anime_Compact's more conservative clean up better preserves this. It also was trained to clean up JPEG 
artifacts, which makes it a great choice since our source video is MPEG2.

Tools were run out of this docker image, the compose.yml at the root folder starts it https://github.com/styler00dollar/VSGAN-tensorrt-docker

To get Docker running I had to install nvidia-container-toolkit (I'm using Linux for all upscale processing). Windows 
users seemed fine as it was.

Extract the model folder into the VSGAN working directory. At the moment, we have to use vs-trt to use it because 
VSGAN is broken, so run this to convert to an engine

I think I had to use ChaiNNer to convert the Pytorch model to an Onnx, then I used the next command to convert it to a 
vs-trt engine.

```commandline
trtexec --fp16 --onnx=path/to/anime_compact.onnx --minShapes=input:1x3x8x8 --optShapes=input:1x3x720x1280 --maxShapes=input:1x3x1080x1920 --saveEngine=path/to/output_compact.engine --tacticSources=+CUDNN,-CUBLAS,-CUBLAS_LT --buildOnly
```

Turn on vs-trt in the inference_config as well as color matching. Then change inference.py to load the correct video.
Then run vspipe with something like

```shell
vspipe -c y4m inference.py - | x264 - --demuxer y4m -o example.mkv

vspipe -c y4m inference.py - | ffmpeg -i pipe: example.mkv -y
```


# Encoding videos for Switch

The Switch is very easy to encode for, it uses WEBM files encoded with a VP9 video and a Vorbis audio stream. Video 
must be 1080p (accidentally gave it 1440p directly from the upscale and it crashed). 

Example ffmpeg command:

```ffmpeg -i opening-cs-aud.mkv -c:v libvpx-vp9 -c:a libvorbis -vf "scale=1920:-1" mvinter01-1080p.webm```

# Encoding and packaging video for PC

The PC release has multiple proprietary containers and codecs involved that make the general process frustrating at 
best and impossible at worst. 

Movie files need to be stored in a CPK, a proprietary CriWare archive format. After attempting to use multiple 
different community tools, we just gave up and used the official CRI File System Tools, which you can find around 
online. Using this, we were able to repackage CoZ's CPK with our own videos, and create our own CPKs.

The game stores video files in CriWare's proprietary USM container, which holds an MPEG2 video stream and an HCA 
audio stream (HCA is a proprietary audio codec also made by CriWare). Encoding for this format has not been 
done successfully yet. We don't want to re-encode video into MPEG2 as it is a very old codec, and both the engine and 
the DirectShow filter it loads should support H264. However, presenting USM files with H264 video to the game causes it 
to hang. 


