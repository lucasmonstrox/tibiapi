import cv2
import numpy as np
from PIL import Image


# TODO: add return type
def load(path: str):
    bgraImage = cv2.imread(path)
    return np.array(bgraImage, dtype=np.uint8)


# TODO: add parameter type
def save(arr, name: str):
    im = Image.fromarray(arr)
    im.save(name)