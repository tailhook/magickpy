__all__ = [
    'image',
    'enums',
    'types',
    'draw',
    ]

import ctypes
import atexit

lib  = ctypes.CDLL('libMagick.so')

lib.MagickCoreGenesis(None, False)

atexit.register(lib.MagickCoreTerminus)

from image import *
from types import *
from enums import *
