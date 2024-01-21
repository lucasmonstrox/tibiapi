from typing import Optional
from tibiapi._common.typings import BBox, Image
from tibiapi.utils.image import cacheObjectPosition, locate
from .config import images


@cacheObjectPosition
def getRadarToolsPosition(screenshot: Image) -> Optional[BBox]:
    return locate(screenshot, images['buttons']['radarTools'])
