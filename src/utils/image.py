import cv2
from farmhash import FarmHash64
import numpy as np
from PIL import Image


def hashit(arr: np.ndarray) -> int:
    return FarmHash64(arr)


def load(path: str) -> np.ndarray:
    bgraImage = cv2.imread(path)
    return np.ascontiguousarray(bgraImage, dtype=np.uint8)


def save(arr: np.ndarray, name: str):
    im = Image.fromarray(arr)
    im.save(name)
