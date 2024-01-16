tibiapi works locating images around the screen through match template [OpenCV](https://opencv.org) function:

```python
from src.utils.image import locate


x, y, width, height = locate(screenshot, battleListIcon)
```

After using "locate" function, coordinates and dimensions of the object are returned and it is now possible to understand where things are.

## Transforming piece of images into data

Before understanding how small pieces of images are transformed into data, tibiapi uses a hash function to often avoid the [OpenCV](https://opencv.org) match template and excessive [CPU](https://en.wikipedia.org/wiki/Central_processing_unit) usage, this is why many functions have responses between [milliseconds](https://simple.wikipedia.org/wiki/Millisecond) and [nanoseconds](https://en.wikipedia.org/wiki/Nanosecond):

```python
import numpy as np
from src.utils.image import hashit


firstValue = np.ascontiguousarray([[1, 2, 3], [4, 5, 6]])
secondValue = np.ascontiguousarray([[1, 2, 3], [4, 5, 6]])
firstValueHash = hashit(firstValue) # will return 56921796602230608
secondValueHash = hashit(secondValue) # will return 56921796602230608
print(firstValueHash == secondValueHash) # True
```

Some areas of the Tibia client screen contain a background with random gray pixels, it would be possible to obtain them with [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition), but this would make the process very slow and instead of using it, a hash system is used after clearing the background to a static black color.

Below in the figure, an example of a fire elemental in the battle list, with grandom gray pixels, before the cleaning process:

![Fire Elemental Dirt](./Fire Elemental Dirt.png)

After the cleaning process, these gray pixels are cleaned by changing them to black pixels:

![Fire Elemental Clean](./Fire Elemental.png)

Now that the image is static and the same as what it contains in tibiapi, getting it from dict will be quickly:

```python
import numpy as np
from src.utils.image import hashit


fireElementalImage = ... # image after cleaning process
fireElementalImageHash = hashit(fireElementalImage)
print(creaturesNamesImagesHashes.get(fireElementalImageHash)) # Will return 'Fire Elemental'
```

The same process is used to obtain the character level, speed, stamina, etc.

## Performance

### Machine code

A lot of [Python](https://www.python.org/downloads/release/python-3117) functions are compiled into machine code through [Numba](https://numba.readthedocs.io/en/stable/) just adding a single decorator. Since tibiapi uses [NumPy](https://numpy.org/doc/stable/) and [Numba](https://numba.readthedocs.io/en/stable/) loves it, which is a big reason for so much performance.

Not all the code is machine code, but it would be ideal, so all the typing would match and [Numba](https://numba.readthedocs.io/en/stable/) would be able to obtain high performance.

### Cache mechanism

Many functions have a [Cache](https://en.wikipedia.org/wiki/Cache_(computing)) mechanism, since some pixels are read from a specific area and it doesn't change, it is not necessary to recalculate the function, just cut out a certain region and obtain the hash of this small image generated, if the hash of this image is the same as the previous one, the value is the same.

Getting the hash from a image is possible using `#!python hashit` function provided in utils module. The response time should vary between 300 and 500 [nanoseconds](https://en.wikipedia.org/wiki/Nanosecond).

### Time magnitude

Small functions such as getting the level, getting the speed, etc., will respond in 5 microseconds, however, as they will be cached, the time will reduce by about 5 times and the response time will be 1 microseconds if the content does not change.
