import cv2
from farmhash import FarmHash64
import numpy as np
from PIL import Image as PilImage
from typing import Callable, Optional
from tibiapi._common.typings import BBox, Image


def cacheObjectPosition(func: Callable) -> Callable:
    lastX = None
    lastY = None
    lastW = None
    lastH = None
    lastImgHash = None

    def inner(screenshot: Image) -> Optional[BBox]:
        nonlocal lastX, lastY, lastW, lastH, lastImgHash
        if lastX != None and lastY != None and lastW != None and lastH != None:
            currentImage = np.ascontiguousarray(
                screenshot[lastY:lastY + lastH, lastX:lastX + lastW])
            if hashit(currentImage) == lastImgHash:
                return (lastX, lastY, lastW, lastH)
        res = func(screenshot)
        if res is None:
            return None
        lastX = res[0]
        lastY = res[1]
        lastW = res[2]
        lastH = res[3]
        currentImage = np.ascontiguousarray(
            screenshot[lastY:lastY + lastH, lastX:lastX + lastW])
        lastImgHash = hashit(currentImage)
        return res
    return inner


def hashit(arr: np.ndarray) -> int:
    return FarmHash64(arr)


def load(path: str) -> Image:
    bgraImage = cv2.imread(path)
    return np.ascontiguousarray(bgraImage, dtype=np.uint8)


def locate(compareImage: np.ndarray, img: np.ndarray, confidence: float = 0.85) -> Optional[BBox]:
    match = cv2.matchTemplate(compareImage, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    if res[1] <= confidence:
        return None
    return res[3][0], res[3][1], len(img[0]), len(img)


def save(arr: np.ndarray, name: str):
    im = PilImage.fromarray(arr)
    im.save(name)
