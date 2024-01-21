from tibiapi.wiki.creatures import creatures as wikiCreatures
from tibiapi.utils.image import load
import pathlib
from numba import typed, types


currentPath = pathlib.Path(__file__).parent.resolve()
creaturesNamesHashes = typed.Dict.empty(
    key_type=types.unicode_type, value_type=types.uint8[:, :, :])
for creature in wikiCreatures:
    creaturesNamesHashes[creature] = load(
        f'{currentPath}/images/monsters/{creature}.png')
