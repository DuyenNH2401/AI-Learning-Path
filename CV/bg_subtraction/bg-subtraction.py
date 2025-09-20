import cv2
import numpy as np

def resize_img(img):
    IMG_SIZE = (678, 318)
    re_img = cv2.resize(img, IMG_SIZE)

    return re_img

def compute_difference(bg_img, input_img):
    diff_3_channel = cv2.absdiff(bg_img, input_img)
    diff_1_channel = np.sum(diff_3_channel, axis = 2) / 3.0
    diff_1_channel = diff_1_channel.astype('uint8')

    return diff_1_channel

def compute_binary_mask(diff_1_channel):
    diff_binary = np.where(diff_1_channel >= 15, 255, 0).astype('uint8')
    diff_binary = np.stack((diff_binary,)*3, axis = -1)

    return diff_binary

def show(img):
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    #input picture
    bg1_img = cv2.imread('GreenBackground.png', 1)
    object_img = cv2.imread('Object.png', 1)
    bg2_img = cv2.imread('NewBackground.jpg', 1)

    #resize picture
    bg1_img = resize_img(bg1_img)
    object_img = resize_img(object_img)
    bg2_img = resize_img(bg2_img)

    #process
    diff_single_channel = compute_difference(bg1_img, object_img)
    binary_mask = compute_binary_mask(diff_single_channel)

    output = np.where(binary_mask == 255, object_img, bg2_img)

    #Display
    show(output)

if __name__ == '__main__':
    main()
