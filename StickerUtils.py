

from random import random
import time


def getStickerEntityData(name) -> str :
    return f"""Entity: { int(time.time()*1000.0) }
TagComponent:
  Tag: {name}
SortComponent:
  Key: 0
TransformComponent:
  Position: [0, 0, 0]
  Rotation: [0, 0, 0]
  Scale: [1, 1, 1]
SpriteComponent:
  Color: [1, 1, 1, 1]
  ScaleType: 0
  Texture: {name}.png
  RespondToTouch : true

"""

def getIndexFileData(name) ->str :
    return f"""Sticker: {name}
Path: {name}.sticker
Type: Static2D
Version: 1
"""