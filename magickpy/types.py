
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
    'ImageMagickException',
    'QuantizeInfo',
    ]

import ctypes
from magickpy import lib
from magickpy.util import wrap_ptr_class
from .enums import ColorspaceType

class PixelPacket(ctypes.Structure):
    _fields_ = [
        ('blue', ctypes.c_ushort),
        ('green', ctypes.c_ushort),
        ('red', ctypes.c_ushort),
        ('opacity', ctypes.c_ushort),
        ]

class MagickPixelPacket(ctypes.Structure):
    _fields_ = [
        ('storage_class', ctypes.c_int),
        ('colorspace', ctypes.c_int),
        ('matte', ctypes.c_int),
        ('fuzz', ctypes.c_double),
        ('depth', ctypes.c_int),
        ('red', ctypes.c_double),
        ('green', ctypes.c_double),
        ('blue', ctypes.c_double),
        ('opacity', ctypes.c_double),
        ('index', ctypes.c_double),
        ]

def scale_to_quantum(f):
    return ctypes.c_ushort(int(f*65535))

class Color(PixelPacket):
    @classmethod
    def rgb(C, r, g, b, a=0):
        return C(*list(map(scale_to_quantum, (b, g, r, a))))

    @classmethod
    def named(C, name):
        exc = ExceptionInfo()
        col = MagickPixelPacket()
        col.colorspace = int(ColorspaceType.RGB)
        name = name.encode('utf-8')
        if not lib.QueryMagickColor(name, ctypes.byref(col), exc):
            raise ImageMagickException(exc)
        return C(*list(map(int, (col.blue, col.green, col.red, col.opacity))))

    def __repr__(self):
        return '<Color: rgba(%d,%d,%d,%d)>' % (self.red, self.green, self.blue, self.opacity)

    def __str__(self):
        return '#%02x%02x%02x%02x' % tuple(v >> 8 for v in (self.red, self.green, self.blue, self.opacity))

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

class GeometryInfo(ctypes.Structure):
    _fields_ = [
        ('rho', ctypes.c_double),
        ('sigma', ctypes.c_double),
        ('xi', ctypes.c_double),
        ('psi', ctypes.c_double),
        ('chi', ctypes.c_double),
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

class _QuantizeInfo(ctypes.Structure):
    _fields_ = [
        ('number_colors', ctypes.c_ulong),
        ('tree_depth', ctypes.c_ulong),
        ('dither', ctypes.c_int),
        ('colorspace', ctypes.c_int),
        ('measure_error', ctypes.c_int),
        ('signature', ctypes.c_ulong),
        ('dither_method', ctypes.c_int),
        ]
QuantizeInfo = wrap_ptr_class(_QuantizeInfo,
    lambda: lib.AcquireQuantizeInfo(None), lib.DestroyQuantizeInfo)

class _ExceptionInfo(ctypes.Structure):
    """ExceptionInfo info for embedding into another structures"""
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
        raise NotImplementedError

ExceptionInfo = wrap_ptr_class(_ExceptionInfo,
    lib.AcquireExceptionInfo, lib.DestroyExceptionInfo)

class ImageMagickException(Exception):
    def __init__(self, exc):
        self.native_exc = exc
        super(ImageMagickException, self).__init__(exc.reason)
