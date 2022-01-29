# Vision

Testing ground for various computer vision tasks / CNN architectures, implemented in tensorflow.

## EM segmentation

![alt text](https://github.com/hongh-zhang/Vision/blob/main/em/data/downsampled/images/train-volume00.jpg "Raw EM image") 
![alt text](https://github.com/hongh-zhang/Vision/blob/main/em/data/cover.gif "Network learning to label membrane")

[Automatic segmentation of neural structure](https://imagej.net/events/isbi-2012-segmentation-challenge), with U-net architecture ([Ronneberger et al., 2015](https://arxiv.org/abs/1505.04597)).

## Pose Estimation

![alt text](https://github.com/hongh-zhang/Vision/blob/main/mice/video.gif "Raw video") 
![alt text](https://github.com/hongh-zhang/Vision/blob/main/mice/snout.gif "Estimated snout position") 
![alt text](https://github.com/hongh-zhang/Vision/blob/main/mice/tail.gif "Estimated tail position") 

Mice pose estimation using methods discussed in [Mathis et al., 2020](https://arxiv.org/abs/2009.00564). 

(Validation, heatmap localization, video labelling WIP)