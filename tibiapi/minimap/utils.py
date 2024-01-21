from typing import Optional
from tibiapi._common.typings import Image
from tibiapi.utils.image import cacheObjectPosition, locate
from .config import images


@cacheObjectPosition
def getRadarToolsPosition(screenshot: Image) -> Optional[tuple[int, int, int, int]]:
    return locate(screenshot, images['buttons']['radarTools'])
