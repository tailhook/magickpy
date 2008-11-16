__all__ = [
    'image',
    'enums',
    'types',
    'draw',
    ]

import ctypes
import atexit

try:
    lib  = ctypes.CDLL('libMagickCore.so')
except OSError:
    lib  = ctypes.CDLL('libMagick.so')

lib.MagickCoreGenesis(None, False)

atexit.register(lib.MagickCoreTerminus)

from image import *
from types import *
from enums import *
from animation import *
