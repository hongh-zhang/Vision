# Vision

Testing ground for various computer vision tasks / CNN architectures, implemented in tensorflow.

## EM segmentation

[Automatic segmentation of neural structure](https://imagej.net/events/isbi-2012-segmentation-challenge), with U-net architecture ([Ronneberger et al., 2015](https://arxiv.org/abs/1505.04597)).

![alt text](https://github.com/hongh-zhang/Vision/blob/main/em/data/downsampled/images/train-volume00.jpg "Raw EM image") 
![alt text](https://github.com/hongh-zhang/Vision/blob/main/em/data/cover.gif "Estimated segmentation")

Network learning to label membrane

## Pose Estimation

Mice pose estimation using methods discussed in [Mathis et al., 2020](https://arxiv.org/abs/2009.00564). 

![alt text](https://github.com/hongh-zhang/Vision/blob/main/mice/data/video.gif "Raw video") 
![alt text](https://github.com/hongh-zhang/Vision/blob/main/mice/data/snout.gif "Estimated snout position") 

Snout position estimation (Refresh the page if it's not synchronous)

![alt text](https://github.com/hongh-zhang/Vision/blob/main/mice/labelled.gif "Labelled video")

[Full video labeling](https://github.com/hongh-zhang/Vision/blob/main/mice/labelled_v1.mp4)

Refining...

##
~~(everything coded in colab)~~ till i reached gpu usage limit