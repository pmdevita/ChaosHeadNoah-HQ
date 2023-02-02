# Transcoding and Archive Handling Notes

# Extracting Xbox360 files
- iso extractor https://github.com/XboxDev/extract-xiso/releases/tag/build-202204252159
- npa extractor https://github.com/Wilhansen/nipa/releases
- video file type: ngs container holding mpeg1 and adpcm

# Converting Steam Movies
- YACpkTool to extract cpk files
- VGMToolbox to demux usm

# Decoding Switch Audio
- vgmstream can decode Switch audio files

# Encoding Switch Audio
- Custom encoder

# Upscaling

I'm no better than a script kiddy at ML, let me know if I got anything wrong.

For the model, I chose sudo_RealESRGAN2x_Dropout_3.799.042_G.pth from here https://upscale.wiki/wiki/Model_Database#Anime. 
From the samples, this seemed to avoid the overly sharp yet blobby lines that were common in some of the 
other models, or even the larger RealESRGAN_x4plus_anime. It looks like it uses this Docker image to 
run https://github.com/styler00dollar/VSGAN-tensorrt-docker

Download the model from the VSGAN-tenorrt-docker repo here https://github.com/styler00dollar/VSGAN-tensorrt-docker/releases

To get Docker running I had to install nvidia-container-toolkit (I'm using Linux for all upscale processing).

Extract the model folder into the VSGAN working directory. At the moment, we have to use vs-trt to use it because 
VSGAN is broken, so run this to convert to an engine
```commandline
trtexec --fp16 --onnx=sudo_RealESRGAN2x_Dropout_3.799.042_opset16.onnx --minShapes=input:1x3x8x8 --optShapes=input:1x3x720x1280 --maxShapes=input:1x3x1080x1920 --saveEngine=model.engine --tacticSources=+CUDNN,-CUBLAS,-CUBLAS_LT --buildOnly
```

Turn on vs-trt in the inference_config as well as color matching. Then change inference.py to load the correct video.
Then run vspipe with something like

```shell
vspipe -c y4m inference.py - | x264 - --demuxer y4m -o example.mkv

vspipe -c y4m inference.py - | ffmpeg -i pipe: example.mkv -y
```



