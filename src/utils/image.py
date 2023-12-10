import cv2
import numpy as np


# TODO: add return type
def load(path: str):
    bgraImage = cv2.imread(path)
    image = np.array(bgraImage, dtype=np.uint8)
    return image
