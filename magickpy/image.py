from magickpy import lib
from magickpy.enums import *
from magickpy.types import *
import ctypes

__all__ = [
    'Image',
    'ImageInfo',
    ]

class ImageInfo(ctypes.Structure):
    _fields_ = [
        ('compression', ctypes.c_int),
        ('orientation', ctypes.c_int),
        ('temporary', ctypes.c_int),
        ('adjoin', ctypes.c_int),
        ('affirm', ctypes.c_int),
        ('antialias', ctypes.c_int),
        ('size', ctypes.c_char_p),
        ('extract', ctypes.c_char_p),
        ('page', ctypes.c_char_p),
        ('scenes', ctypes.c_char_p),
        ('scene', ctypes.c_ulong),
        ('number_scenes', ctypes.c_ulong),
        ('depth', ctypes.c_ulong),
        ('inteface', ctypes.c_int),
        ('endian', ctypes.c_int),
        ('units', ctypes.c_int),
        ('quality', ctypes.c_ulong),
        ('sampling_factor', ctypes.c_char_p),
        ('server_name', ctypes.c_char_p),
        ('font', ctypes.c_char_p),
        ('texture', ctypes.c_char_p),
        ('density', ctypes.c_char_p),
        ('pointsize', ctypes.c_double),
        ('fuzz', ctypes.c_double),
        ('background_color', PixelPacket),
        ('border_color', PixelPacket),
        ('matte_color', PixelPacket),
        ('dither', ctypes.c_int),
        ('mnochrome', ctypes.c_int),
        ('colors', ctypes.c_ulong),
        ('colorspace', ctypes.c_int),
        ('type', ctypes.c_int),
        ('preview_type', ctypes.c_int),
        ('group', ctypes.c_long),
        ('ping', ctypes.c_int),
        ('verbose', ctypes.c_int),
        ('view', ctypes.c_char_p),
        ('authenticate', ctypes.c_char_p),
        ('channel', ctypes.c_int),
        ('attributes', ctypes.c_void_p),
        ('options', ctypes.c_void_p),
        ('progress_monitor', ctypes.c_void_p),
        ('client_data', ctypes.c_void_p),
        ('cache', ctypes.c_void_p),
        ('stream', ctypes.c_void_p),
        ('file', ctypes.c_void_p),
        ('blob', ctypes.c_void_p),
        ('length', ctypes.c_ulong),
        ('magick', ctypes.c_char * 4096),
        ('unique', ctypes.c_char * 4096),
        ('zero', ctypes.c_char * 4096),
        ('filename', ctypes.c_char * 4096),
        ('debug', ctypes.c_int),
        ('tile', ctypes.c_char_p),
        ('subimage', ctypes.c_ulong),
        ('subrange', ctypes.c_ulong),
        ('pen', PixelPacket),
        ('signature', ctypes.c_ulong),
        ('virtual_pixel_method', ctypes.c_void_p),
        ('transparent_color', PixelPacket),
        ('profile', ctypes.c_void_p),
        ]
    def __new__(C):
        return CloneImageInfo(None).contents
    def __del__(self):
        return lib.DestroyImageInfo(ctypes.byref(self))

PImageInfo = ctypes.POINTER(ImageInfo)

wrapinit = []
FwPImage = object()

def new_image_wrapper(fun, *args):
    args = [FwPImage] + list(args) + [ctypes.POINTER(ExceptionInfo)]
    def func(self, *args):
        exc = ExceptionInfo()
        args = [self] + list(args) + [exc]
        res = fun(*args)
        if not res:
            raise ImageMagickError(exc)
        return res.contents
    wrapinit.append((fun, args))
    return func

def apply_image_wrapper(fun, *args):
    args = [FwPImage] + list(args)
    def func(self, *args):
        args = [self] + list(args)
        res = fun(*args)
        if not res:
            raise ImageMagickError(self.exception)
    wrapinit.append((fun, args))
    return func

def init_image_wrapper(fun, args):
    for (i, x) in enumerate(args):
        if x is FwPImage:
            args[i] = PImage
    fun.argtypes = args
    fun.restype = PImage

class Image(ctypes.Structure):

    def __new__(C):
        return AllocateImage(None).contents
    @classmethod
    def read(C, file):
        if isinstance(file, basestring):
            inf = ImageInfo()
            inf.filename = file
            exinfo = ExceptionInfo()
            res = ReadImage(ctypes.byref(inf), ctypes.byref(exinfo))
            if not res:
                raise ImageMagickException(exinfo)
            return res.contents
        else:
            raise NotImplementedError

    @classmethod
    def create(C, width, height, color):
        inf = ImageInfo()
        res = lib.NewMagickImage(ctypes.byref(inf), width, height, ctypes.byref(color))
        if not res:
            raise ImageMagickException(inf.exception)
        im = ctypes.cast(res, PImage).contents
        im.setColorspace(ColorspaceType.RGB)
        im.setBackgroundColor(color)
        return im

    def write(self, file):
        if isinstance(file, basestring):
            inf = ImageInfo()
            self.filename = file
            if not lib.WriteImage(ctypes.byref(inf), ctypes.byref(self)):
                raise ImageMagickException(self.exception)
            return True
        else:
            raise NotImplementedError

    def __nonzero__(self):
        return True

    @property
    def width(self):
        return self.columns

    @property
    def height(self):
        return self.rows

    def draw(self, string):
        inf = DrawInfo()
        buf = ctypes.c_buffer(string)
        inf.primitive = ctypes.cast(buf, ctypes.c_char_p)
        inf.fill = Color.rgb(1, 1, 1)
        if not lib.DrawImage(ctypes.byref(self), ctypes.byref(inf)):
            raise ImageMagickException(self.exception)

    def makeCrop(self, geometry_or_width, height=None, x=None, y=None):
        if height is None:
            return self._crop(geometry_or_width)
        geom = RectangleInfo(geometry_or_width, height, x, y)
        return self._makeCrop(geom)

    def makeColorize(self, color, opacity_r, opacity_g=None, opacity_b=None):
        if isinstance(opacity_r, basestring):
            opacity = opacity_r
        else:
            if opacity_g is None:
                opacity_g = opacity_r
            if opacity_b is None:
                opacity_b = opacity_r
            opacity = "%u/%u/%u" % (opacity_r, opacity_g, opacity_b)
        return self._makeColorize(opacity, color)

    _makeCrop = new_image_wrapper(lib.CropImage, ctypes.POINTER(RectangleInfo))
    makeBlur = new_image_wrapper(lib.BlurImage, ctypes.c_double, ctypes.c_double)
    makeAdaptiveBlur = new_image_wrapper(lib.AdaptiveBlurImage, ctypes.c_double, ctypes.c_double)
    makeGaussianBlur = new_image_wrapper(lib.GaussianBlurImage, ctypes.c_double, ctypes.c_double)
    makeMotionBlur = new_image_wrapper(lib.MotionBlurImage, ctypes.c_double, ctypes.c_double, ctypes.c_double)
    makeShade = new_image_wrapper(lib.ShadeImage, ctypes.c_int, ctypes.c_double, ctypes.c_double)
    _makeColorize = new_image_wrapper(lib.ColorizeImage, ctypes.c_char_p, Color)
    makeThumbnail = new_image_wrapper(lib.ThumbnailImage, ctypes.c_ulong, ctypes.c_ulong)
    makeScale = new_image_wrapper(lib.ScaleImage, ctypes.c_ulong, ctypes.c_ulong)
    makeSample = new_image_wrapper(lib.SampleImage, ctypes.c_ulong, ctypes.c_ulong)
    makeResize = new_image_wrapper(lib.ResizeImage, ctypes.c_ulong, ctypes.c_ulong, FilterTypes, ctypes.c_double)

    applyContrastStretch = apply_image_wrapper(lib.ContrastStretchImage, ctypes.c_char_p)
    applyNormalize = apply_image_wrapper(lib.NormalizeImage)
    applyComposite = apply_image_wrapper(lib.CompositeImage, CompositeOp, FwPImage, ctypes.c_int, ctypes.c_int)
    applySigmoidalContrast = apply_image_wrapper(lib.SigmoidalContrastImage, ctypes.c_int, ctypes.c_char_p)
    applySeparateChannel = apply_image_wrapper(lib.SeparateImageChannel, ChannelType)
    applyNegate = apply_image_wrapper(lib.NegateImage, ctypes.c_int)

    setColorspace = apply_image_wrapper(lib.SetImageColorspace, ColorspaceType)

    def copy(self):
        exc = ExceptionInfo()
        res = ctypes.cast(lib.CloneImage(ctypes.byref(self), 0, 0, True, ctypes.byref(exc)), PImage)
        if not res:
            raise ImageMagickException(exc)
        return res.contents

    def setBackgroundColor(self, color):
        self.background_color = color
        lib.SetImageBackgroundColor(ctypes.byref(self))

    def setMatte(self, value):
        if bool(value) != bool(self.matte):
            lib.SetImageOpacity(ctypes.byref(self), OpaqueOpacity)

    def setVirtualPixelMethod(self, value):
        lib.SetImageVirtualPixelMethod(ctypes.byref(self), int(value))

    def __del__(self):
        lib.DestroyImage(ctypes.byref(self))

Image._fields_ = [
        ('storage_class', ctypes.c_int),
        ('colorspace', ctypes.c_int),
        ('compression', ctypes.c_int),
        ('quality', ctypes.c_ulong),
        ('operation', ctypes.c_int),
        ('taint', ctypes.c_int),
        ('matte', ctypes.c_int),
        ('columns', ctypes.c_ulong),
        ('rows', ctypes.c_ulong),
        ('depth', ctypes.c_ulong),
        ('colors', ctypes.c_ulong),
        ('colormap', ctypes.POINTER(PixelPacket)),
        ('background_color', PixelPacket),
        ('border_color', PixelPacket),
        ('matte_color', PixelPacket),
        ('gamma', ctypes.c_double),
        ('chromaticity', ChromaticityInfo),
        ('rendering_intent', ctypes.c_int),
        ('profiles', ctypes.c_void_p),
        ('units', ctypes.c_int),
        ('montage', ctypes.c_char_p),
        ('directory', ctypes.c_char_p),
        ('geometry', ctypes.c_char_p),
        ('offset', ctypes.c_long),
        ('x_resolution', ctypes.c_double),
        ('y_resolution', ctypes.c_double),
        ('page', RectangleInfo),
        ('extract_info', RectangleInfo),
        ('the_info', RectangleInfo),
        ('bias', ctypes.c_double),
        ('blur', ctypes.c_double),
        ('fuzz', ctypes.c_double),
        ('filter', ctypes.c_int),
        ('interlace', ctypes.c_int),
        ('endian', ctypes.c_int),
        ('gravity', ctypes.c_int),
        ('compose', ctypes.c_int),
        ('dispose', ctypes.c_int),
        ('clip_mask', ctypes.POINTER(Image)),
        ('scene', ctypes.c_ulong),
        ('delay', ctypes.c_ulong),
        ('ticks_per_second', ctypes.c_long),
        ('iterations', ctypes.c_ulong),
        ('total_colors', ctypes.c_ulong),
        ('start_loop', ctypes.c_long),
        ('error', ErrorInfo),
        ('timer', TimerInfo),
        ('progress_monitor', ctypes.c_int),
        ('client_data', ctypes.c_void_p),
        ('cache', ctypes.c_void_p),
        ('attributes', ctypes.c_void_p),
        ('ascii85', ctypes.c_void_p),
        ('blob', ctypes.c_void_p),
        ('filename', ctypes.c_char * 4096),
        ('magick_filename', ctypes.c_char * 4096),
        ('magick', ctypes.c_char * 4096),
        ('magick_columns', ctypes.c_ulong),
        ('magick_rows', ctypes.c_ulong),
        ('exception', SafeExceptionInfo),
        ('debug', ctypes.c_int),
        ('reference_count', ctypes.c_long),
        ('semaphore', ctypes.c_void_p),
        ('color_profile', ProfileInfo),
        ('iptc_profile', ProfileInfo),
        ('generic_profile', ctypes.POINTER(ProfileInfo)),
        ('generic_profiles', ctypes.c_ulong),
        ('signature', ctypes.c_ulong),
        ('previous', ctypes.POINTER(Image)),
        ('list', ctypes.POINTER(Image)),
        ('next', ctypes.POINTER(Image)),
        ('interpolate', ctypes.c_int),
        ('black_point_compensation', ctypes.c_int),
        ('transparent_color', PixelPacket),
        ('mask', ctypes.POINTER(Image)),
        ('tile_offset', RectangleInfo),
        ('properties', ctypes.c_void_p),
        ('artifacts', ctypes.c_void_p),
        ]

PImage = ctypes.POINTER(Image)

for w in wrapinit:
    init_image_wrapper(*w)

## Constants
OpaqueOpacity = 0
TransparentOpacity = 65535

## Functions

CloneImageInfo = lib.CloneImageInfo
CloneImageInfo.restype = PImageInfo

AllocateImage = lib.AllocateImage
AllocateImage.restype = PImage

ReadImage = lib.ReadImage
ReadImage.restype = PImage

from magickpy.draw import DrawInfo #avoiding circular import
