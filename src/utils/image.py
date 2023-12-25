import cv2
from farmhash import FarmHash64
import numpy as np
from PIL import Image
from typing import Optional


def hashit(arr: np.ndarray) -> int:
    return FarmHash64(arr)


def load(path: str) -> np.ndarray:
    bgraImage = cv2.imread(path)
    return np.ascontiguousarray(bgraImage, dtype=np.uint8)


def locate(compareImage: np.ndarray, img: np.ndarray, confidence: float = 0.85) -> Optional[tuple[int, int, int, int]]:
    match = cv2.matchTemplate(compareImage, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    if res[1] <= confidence:
        return None
    return res[3][0], res[3][1], len(img[0]), len(img)


def save(arr: np.ndarray, name: str):
    im = Image.fromarray(arr)
    im.save(name)
