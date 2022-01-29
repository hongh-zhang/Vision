import os
import cv2

def downsample(in_fld, out_fld):

    for img_file in os.listdir(in_fld):
        img = cv2.imread(os.path.join(in_fld, img_file), cv2.IMREAD_GRAYSCALE)
        img = cv2.pyrDown(img)
        cv2.imwrite(os.path.join(out_fld, img_file), img)


if __name__ == '__main__':

    downsample('original/images', 'downsampled/images')
    downsample('original/labels', 'downsampled/labels')
    print('done')
