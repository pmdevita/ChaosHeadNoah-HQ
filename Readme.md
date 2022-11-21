# Chaos;Head NOAH HQ Patch

A higher quality assets patch for the Switch/Steam release of Chaos;Head.

Not only is the English release of Chaos;Head NOAH poorly localized and rife with bugs, the assets  
have been severely and improperly compressed. The most noticeable example is the videos and background 
images. The Switch/Steam release is in 1080p, which should have been
an improvement over the original 720p Xbox 360 release. However, there is so much artifacting in the 
images and videos that the perceived quality is actually lower.
This patch aims to fix these issues with a few subprojects.

## Cutscene Re-encoding

We need to match up the original Xbox cutscenes with the corresponding Switch and Steam files, 
then rescale to 1080p and properly transcode the result. We're going to attempt to do an AI upscale 
to try to and improve the quality a bit more over a simple rescale, you can see some notes about 
that in the [transcoding notes](docs/transcode_notes.md).

### Examples

The opening cutscene is particularly garish. In general, the visual difference between the 
Switch and Steam release is minimal, so they will be used interchangeably in comparisons.
The Xbox images are smaller because it uses smaller images, the cuts are done proportionally.

There are also some slight changes in color, I'll have to double-check if I messed up the color space.

For this one, notice how the details for the light rays are completely mushed. The hand has 
also been reduced to a single shade of white.
 
| Xbox                                         | Switch/Steam                                    |
|----------------------------------------------|-------------------------------------------------|
| ![Xbox BG 1](comparisons/mv_1_xbox_crop.png) | ![Switch BG 1](comparisons/mv_1_steam_crop.png) |

There is some banding here too on the Xbox version, but it's far blockier on the Switch/Steam.

| Xbox                                         | Switch/Steam                                    |
|----------------------------------------------|-------------------------------------------------|
| ![Xbox BG 2](comparisons/mv_2_xbox_crop.png) | ![Switch BG 2](comparisons/mv_2_steam_crop.png) |

Both of these are bad but the Switch/Steam version has far steeper jumps in the gradient.

| Xbox                                    | Switch/Steam                                |
|-----------------------------------------|---------------------------------------------|
| ![Xbox BG 4](comparisons/mv_4_xbox.png) | ![Switch BG 4](comparisons/mv_4_steam.png) |



## BG Image Re-encoding

Similarly to the cutscenes, we need to match all of the image files up and then upscale and
re-encode them. We'll also be attempting an AI upscale with this as well.

It's a bit difficult to demonstrate in a Readme, especially in light mode, but if you zoom into both of these images, you'll notice a lot more 
blocking in the Switch version than the Xbox one. The Xbox image has a smoother gradient. I'm working on pulling out more examples.

### Examples

| Xbox                                 | Switch/Steam                             |
|--------------------------------------|------------------------------------------|
| ![Xbox BG 1](comparisons/1_xbox.png) | ![Switch BG 1](comparisons/1_switch.png) |

## Switch Audio Re-encoding

Nintendo provides an Opus encoder as part of their SDK for the Switch. For some horrifying reason,
they wrote their own encoder, and it's [worse than the open source reference one](https://twitter.com/masagratordev/status/1571210220696702977).
To fix this, we can re-encode the voice lines and music from the Steam release again for the 
Switch release with a [modified Opus encoder](https://github.com/pmdevita/NXAEncode_ChaosHead) that writes out Nintendo's format.

I was unable to differentiate the voice lines between the Switch and Steam releases in a blind test
so for right now, this project is shelved since returns will likely be minimal to none. Music still 
needs to be investigated.


# Contributing/Help

Right now, I need some help with matching Xbox assets to Switch/Steam assets. If you've already played 
the game or don't care about spoilers, please add me on Discord ptrharmonic#9765. If you have experience
with Docker and own an Nvidia GPU, I could also use some help with upscaling the videos and images.


# Compatibility with the Committee of Zero Patch

CoZ's patch isn't released at the moment, so I'm not entirely sure what the situation will look like. But,
the aim is for this patch to be compatible. The one potential point of friction might be 
with videos that CoZ has subtitled, we'll either need to remake the subs on our own or look into 
some kind of collaboration.
