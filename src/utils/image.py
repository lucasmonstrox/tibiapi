import cv2
import numpy as np
from PIL import Image


def load(path: str) -> np.ndarray:
    bgraImage = cv2.imread(path)
    return np.array(bgraImage, dtype=np.uint8)


def save(arr: np.ndarray, name: str):
    im = Image.fromarray(arr)
    im.save(name)
