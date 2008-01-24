
__all__ = [
    'PixelPacket',
    'Color',
    'ChromaticityInfo',
    'RectangleInfo',
    'ErrorInfo',
    'Timer',
    'TimerInfo',
    'ProfileInfo',
    'ExceptionInfo',
    'PExceptionInfo',
    'ImageMagickException',
    ]

import ctypes
from magickpy import lib

class PixelPacket(ctypes.Structure):
    _fields_ = [
        ('blue', ctypes.c_short),
        ('green', ctypes.c_short),
        ('red', ctypes.c_short),
        ('opacity', ctypes.c_short),
        ]

def scale_to_quantum(f):
    return ctypes.c_short(int(f*65535))

class Color(PixelPacket):
    def __new__(C, r, g, b):
        return super(Color, C).__new__(C, *map(scale_to_quantum, (r, g, b)))
    def __init__(C, r, g, b):
        return super(Color, C).__init__(*map(scale_to_quantum, (r, g, b)))

class PrimaryInfo(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_double),
        ('y', ctypes.c_double),
        ('z', ctypes.c_double),
        ]

class ChromaticityInfo(ctypes.Structure):
    _fields_ = [
        ('red_primary', PrimaryInfo),
        ('green_primary', PrimaryInfo),
        ('blue_primary', PrimaryInfo),
        ('white_point', PrimaryInfo),
        ]

class RectangleInfo(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_ulong),
        ('height', ctypes.c_ulong),
        ('x', ctypes.c_long),
        ('y', ctypes.c_long),
        ]

class ErrorInfo(ctypes.Structure):
    _fields_ = [
        ('mean_error_per_pixel', ctypes.c_double),
        ('normalized_mean_error', ctypes.c_double),
        ('normalized_maximum_error', ctypes.c_double),
        ]

class Timer(ctypes.Structure):
    _fields_ = [
        ('start', ctypes.c_double),
        ('stop', ctypes.c_double),
        ('total', ctypes.c_double),
        ]

class TimerInfo(ctypes.Structure):
    _fields_ = [
        ('user', Timer),
        ('elapsed', Timer),
        ('state', ctypes.c_int),
        ('signature', ctypes.c_ulong),
        ]

class ProfileInfo(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('length', ctypes.c_ulong),
        ('info', ctypes.POINTER(ctypes.c_byte)),
        ('signature', ctypes.c_ulong),
        ]

class ExceptionInfo(ctypes.Structure):
    _fields_ = [
        ('severity', ctypes.c_int),
        ('error_number', ctypes.c_int),
        ('reason', ctypes.c_char_p),
        ('description', ctypes.c_char_p),
        ('exceptions', ctypes.c_void_p),
        ('relinquish', ctypes.c_int),
        ('semaphore', ctypes.c_void_p),
        ('signature', ctypes.c_ulong),
        ]
    def __new__(self):
        return AcquireExceptionInfo().contents
    def __del__(self):
        lib.DestroyExceptionInfo(ctypes.byref(self))

PExceptionInfo = ctypes.POINTER(ExceptionInfo)

class ImageMagickException(Exception):
    def __init__(self, exc):
        self.native_exc = exc
        super(ImageMagickException, self).__init__(exc.reason)

AcquireExceptionInfo = lib.AcquireExceptionInfo
AcquireExceptionInfo.restype = PExceptionInfo
