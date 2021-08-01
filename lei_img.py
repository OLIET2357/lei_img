import cv2
import numpy as np
import struct


def lei_img(FILE):
    buf = open(FILE, 'rb').read()

    header = buf[:8]
    WIDTH, = struct.unpack('<L', header[0:4])
    HEIGHT, = struct.unpack('<L', header[4:8])
    HEIGHT = HEIGHT//2*3

    data = buf[8:]
    assert len(data) == WIDTH*HEIGHT*2

    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    for i in range(len(data)//2):
        word, = struct.unpack('<H', data[i*2:i*2+2])
        r = (word & 0b1111100000000000) >> 11 << 3
        g = (word & 0b0000011111100000) >> 5 << 2
        b = (word & 0b0000000000011111) >> 0 << 3
        img[i//WIDTH, i % WIDTH] = [b, g, r]
    return img
