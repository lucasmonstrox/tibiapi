Using tibia is very easy, you just need to import API functions and pass the Tibia client screenshot image in BGRA format:

```py
import numpy as np
from tibiapi.battleList import BattleList
from tibiapi._common import RectImage

image = np.array([...], dtype=np.uint8) # must be an BGRA image converted into NumPy array using uint8 to gain performance
battleListImage = RectImage(0, 0, image)
battleList = BattleList(battleListImage)
battleList.creatures() # will return battle list creatures ['Dragon', 'Dragon Lord']
```

You can go to [API reference](../api/battle-list/battle-list.md) and discover more tibiapi functions.
