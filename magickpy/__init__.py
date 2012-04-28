__all__ = [
    'image',
    'enums',
    'types',
    'draw',
    ]

import ctypes
import atexit

for dll_name in ('libMagickCore.so', 'libMagick.so', 'CORE_RL_magick_.dll'):
    try:
        lib = ctypes.CDLL(dll_name)
    except OSError:
        pass
    else:
        break
else:
    raise RuntimeError("Can't find imagemagick dll")

lib.MagickCoreGenesis(None, False)
lib.SetMagickMemoryMethods(
    ctypes.pythonapi.PyMem_Malloc,
    ctypes.pythonapi.PyMem_Realloc,
    ctypes.pythonapi.PyMem_Free)

atexit.register(lib.MagickCoreTerminus)

from .image import *
from .types import *
from .enums import *
from .animation import *
