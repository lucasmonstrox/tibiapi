import cv2
import numpy as np
from PIL import Image
import xxhash


def hashit(arr: np.ndarray) -> int:
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).intdigest()


def load(path: str) -> np.ndarray:
    bgraImage = cv2.imread(path)
    return np.array(bgraImage, dtype=np.uint8)


def save(arr: np.ndarray, name: str):
    im = Image.fromarray(arr)
    im.save(name)
