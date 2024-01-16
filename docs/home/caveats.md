Obtaining as much information from the game and making it available in the API even though it is a difficult job since not everything is available due to randomness or certain things are not visible on the screen.

### Blockable objects

Detecting objects in the game window requires [computer vision](https://en.wikipedia.org/wiki/Computer_vision), to solve this problem, tibiapi will implement [Detectron2](https://github.com/facebookresearch/detectron2) or [YOLO](https://github.com/ultralytics/ultralytics) as soon as possible.

Since detecting objects is not implemented, marking the coordinate as "unwalkable" for a short period of time is a good option.

### Invisible creatures

Getting invisible creatures is not possible, but "wiki" module provides which creatures can become invisible at any time, sometimes they appear on the screen and can be attacked in that area with [Runes](https://tibia.fandom.com/wiki/Runes) or by [Spells](https://tibia.fandom.com/wiki/Spells) when the character is close and blocked by invisible creature.

### Players on screen

Parsing players names doesn't have the same assertiveness as [Creatures](https://tibia.fandom.com/wiki/Creatures) or [NPCs](https://tibia.fandom.com/wiki/NPCs) since these have a fixed name in the battle list and tibiapi has kept this in memory, while players have random names and sometimes with ellipsis in the battle list.

Getting it through [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) would be impractical and slow, which is not the purpose of tibiapi, but, tibiapi can categorize what is a [Creatures](https://tibia.fandom.com/wiki/Creatures), what is [Familiars](https://tibia.fandom.com/wiki/Familiars), what is [NPCs](https://tibia.fandom.com/wiki/NPCs) and what is left is categorized as a Players.
