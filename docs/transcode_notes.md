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

For the model, I chose sudo_RealESRGAN2x_Dropout_3.799.042_G.pth from here https://upscale.wiki/wiki/Model_Database#Anime. 
From the samples, this seemed to avoid the overly sharp yet blobby lines that were common in some of the 
other models, or even the larger RealESRGAN_x4plus_anime. It looks like it uses this Docker image to 
run https://github.com/styler00dollar/VSGAN-tensorrt-docker

