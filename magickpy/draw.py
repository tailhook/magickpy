
__all__ = [
    'SegmentInfo',
    'AffineMatrix',
    'GradientInfo',
    ]

import ctypes
from magickpy.image import Image
from magickpy.types import RectangleInfo, PixelPacket
from magickpy.enums import CompositeOp
from magickpy.util import wrap_ptr_class
from magickpy import lib

class SegmentInfo(ctypes.Structure):
    _fields_ = [
        ('x1', ctypes.c_double),
        ('y1', ctypes.c_double),
        ('x2', ctypes.c_double),
        ('y2', ctypes.c_double),
        ]

class AffineMatrix(ctypes.Structure):
    _fields_ = [
        ('sx', ctypes.c_double),
        ('rx', ctypes.c_double),
        ('ry', ctypes.c_double),
        ('sy', ctypes.c_double),
        ('tx', ctypes.c_double),
        ('ty', ctypes.c_double),
        ]

class GradientInfo(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_int),
        ('bounding_box', RectangleInfo),
        ('gradient_vector', SegmentInfo),
        ('stops', ctypes.c_void_p),
        ('number_stops', ctypes.c_ulong),
        ('spread', ctypes.c_int),
        ('debug', ctypes.c_int),
        ('signature', ctypes.c_ulong),
        ]
    def __new__(self):
        raise NotImplementedError

class ElementReference(ctypes.Structure):
    def __new__(self):
        raise NotImplementedError
ElementReference._fields_ = [
        ('id', ctypes.c_char_p),
        ('type', ctypes.c_int),
        ('gradient', GradientInfo),
        ('signature', ctypes.c_ulong),
        ('previous', ctypes.POINTER(ElementReference)),
        ('next', ctypes.POINTER(ElementReference)),
    ]

class _DrawInfo(ctypes.Structure):
    _fields_ = [
        ('primitive', ctypes.c_char_p),
        ('geometry', ctypes.c_char_p),
        ('viewbox', RectangleInfo),
        ('affine', AffineMatrix),
        ('gravity', ctypes.c_int),
        ('fill', PixelPacket),
        ('stroke', PixelPacket),
        ('stroke_width', ctypes.c_double),
        ('gradient', GradientInfo),
        ('fill_pattern', Image),
        ('tile', Image),
        ('stroke_pattern', Image),
        ('stroke_antialias', ctypes.c_int),
        ('text_antialias', ctypes.c_int),
        ('fill_fule', ctypes.c_int),
        ('linecap', ctypes.c_int),
        ('linejoin', ctypes.c_int),
        ('miterlimit', ctypes.c_ulong),
        ('dash_offset', ctypes.c_double),
        ('decorate', ctypes.c_int),
        ('compose', ctypes.c_int),
        ('text', ctypes.c_char_p),
        ('face', ctypes.c_ulong),
        ('font', ctypes.c_char_p),
        ('metrics', ctypes.c_char_p),
        ('family', ctypes.c_char_p),
        ('style', ctypes.c_int),
        ('stretch', ctypes.c_int),
        ('weight', ctypes.c_ulong),
        ('encoding', ctypes.c_char_p),
        ('pointsize', ctypes.c_double),
        ('density', ctypes.c_char_p),
        ('align', ctypes.c_int),
        ('undercolor', PixelPacket),
        ('border_color', PixelPacket),
        ('server_name', ctypes.c_char_p),
        ('dash_pattern', ctypes.c_double),
        ('clip_mask', ctypes.c_char_p),
        ('bounds', SegmentInfo),
        ('clip_units', ctypes.c_int),
        ('opacity', ctypes.c_short),
        ('render', ctypes.c_int),
        ('element_reference', ElementReference),
        ('debug', ctypes.c_int),
        ('signature', ctypes.c_ulong),
        ]

DrawInfo = wrap_ptr_class(_DrawInfo, lib.AcquireDrawInfo, lib.DestroyDrawInfo)
