from magickpy import lib
from magickpy.util import wrap_ptr_class
from magickpy.enums import *
from magickpy.types import (_ExceptionInfo, ExceptionInfo,
    TimerInfo, ProfileInfo, ImageMagickException,
    GeometryInfo, QuantizeInfo,
    PixelPacket, Color, RectangleInfo, ChromaticityInfo, ErrorInfo)
import ctypes

__all__ = [
    'Image',
    'ImageInfo',
    ]

class _ImageInfo(ctypes.Structure):
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

ImageInfo = wrap_ptr_class(_ImageInfo, lib.AcquireImageInfo, lib.DestroyImageInfo)

class _Image(ctypes.Structure):
    pass

_Image._fields_ = [
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
        ('clip_mask', ctypes.POINTER(_Image)),
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
        ('exception', _ExceptionInfo),
        ('debug', ctypes.c_int),
        ('reference_count', ctypes.c_long),
        ('semaphore', ctypes.c_void_p),
        ('color_profile', ProfileInfo),
        ('iptc_profile', ProfileInfo),
        ('generic_profile', ctypes.POINTER(ProfileInfo)),
        ('generic_profiles', ctypes.c_ulong),
        ('signature', ctypes.c_ulong),
        ('previous', ctypes.c_void_p),
        ('list', ctypes.c_void_p),
        ('next', ctypes.c_void_p),
        ('interpolate', ctypes.c_int),
        ('black_point_compensation', ctypes.c_int),
        ('transparent_color', PixelPacket),
        ('mask', ctypes.POINTER(_Image)),
        ('tile_offset', RectangleInfo),
        ('properties', ctypes.c_void_p),
        ('artifacts', ctypes.c_void_p),
        ]


def new_image_wrapper(fun, *args):
    args = [_PImage] + list(args) + [ExceptionInfo]
    fun.argtypes = args
    def func(self, *args):
        exc = ExceptionInfo()
        args = [self] + list(args) + [exc]
        res = fun(*args)
        if not res:
            raise ImageMagickException(exc)
        return Image(res)
    return func

def apply_image_wrapper(fun, *args):
    args = [_PImage] + list(args)
    fun.argtypes = args
    def func(self, *args):
        args = [self] + list(args)
        res = fun(*args)
        if not res:
            if self.exception:
                raise ImageMagickException(self.exception)
        return bool(res)
    return func

_PImage = wrap_ptr_class(_Image, lambda:lib.AllocateImage(None), lib.DestroyImage, classname="_PImage")

class PixelWrapper(object):
    def __init__(self, im, x, y, w, h):
        self.im = im
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __enter__(self):
        exc = ExceptionInfo()
        px = lib.GetAuthenticPixels(self.im, self.x, self.y, self.w, self.h, exc)
        if not px:
            raise ImageMagickException(exc)
        self.px = ctypes.cast(px, ctypes.POINTER(PixelPacket*(self.w*self.h)))
        return self

    def __exit__(self, A, B, C):
        del self.px
        exc = ExceptionInfo()
        lib.SyncAuthenticPixels(self.im, exc)
        del self.im

    def __setitem__(self, coord, value):
        x, y = coord
        if x >= self.w or y >= self.h or x < 0 or y < 0:
            raise ValueError("Wrong coordinates %d, %d" % (x, y))
        if not isinstance(value, PixelPacket):
            value = PixelPacket(*value)
        self.px[0][y*self.w+x] = value

    def __getitem__(self, coord):
        x, y = coord
        if x >= self.w or y >= self.h or x < 0 or y < 0:
            raise ValueError("Wrong coordinates %d, %d" % (x, y))
        return self.px[0][y*self.w+x]

class Image(_PImage):
    @classmethod
    def read(C, file):
        if isinstance(file, str):
            inf = ImageInfo()
            inf.filename = file
            exinfo = ExceptionInfo()
            res = lib.ReadImage(inf, exinfo)
            if not res:
                raise ImageMagickException(exinfo)
            return C(res)
        else:
            raise NotImplementedError

    @classmethod
    def tile(C, file, width, height):
        if isinstance(file, str):
            inf = ImageInfo()
            file = 'tile:' + file
            inf.size = "%dx%d" % (width, height)
            inf.filename = file
            try:
                exinfo = ExceptionInfo()
                res = lib.ReadImage(inf, exinfo)
                if not res:
                    raise ImageMagickException(exinfo)
                return C(res)
            finally:
                inf.size = 0
                inf.file = 0
        else:
            raise NotImplementedError

    @classmethod
    def ping(C, file):
        if isinstance(file, str):
            inf = ImageInfo()
            inf.filename = file
            exinfo = ExceptionInfo()
            res = lib.PingImage(inf, exinfo)
            if not res:
                raise ImageMagickException(exinfo)
            return C(res)
        else:
            raise NotImplementedError

    @classmethod
    def create(C, width, height, color):
        inf = ImageInfo()
        res = lib.NewMagickImage(inf, width, height, ctypes.byref(color))
        if not res:
            raise ImageMagickException(inf.exception)
        im = C(res)
        im.setColorspace(ColorspaceType.RGB)
        im.setBackgroundColor(color)
        return im

    def write(self, file):
        if isinstance(file, str):
            inf = ImageInfo()
            self.filename = file
            if not lib.WriteImage(inf, self):
                raise ImageMagickException(self.exception)
            return True
        else:
            raise NotImplementedError

    def display(self):
            inf = ImageInfo()
            res = lib.DisplayImages(inf, self)
            if not res:
                raise ImageMagickException(self.exception)

    def __bool__(self):
        return True

    @property
    def width(self):
        return self.columns

    @property
    def height(self):
        return self.rows

    def draw(self, string):
        inf = DrawInfo()
        buf = ctypes.c_buffer(string.encode('utf-8'))
        inf.primitive = ctypes.cast(buf, ctypes.c_char_p)
        try:
            if not lib.DrawImage(self.value, inf):
                raise ImageMagickException(self.exception)
        finally:
            inf.primitive = 0

    def makeCrop(self, geometry_or_width, height=None, x=None, y=None):
        if height is None:
            return self._crop(geometry_or_width)
        geom = RectangleInfo(geometry_or_width, height, x, y)
        return self._makeCrop(geom)

    def makeColorize(self, color, opacity_r, opacity_g=None, opacity_b=None):
        if isinstance(opacity_r, str):
            opacity = opacity_r
        else:
            if opacity_g is None:
                opacity_g = opacity_r
            if opacity_b is None:
                opacity_b = opacity_r
            opacity = "%u/%u/%u" % (opacity_r, opacity_g, opacity_b)
        return self._makeColorize(opacity.encode('ascii'), color)

    def copyPixels(self, source, sx, sy, w, h, tx, ty):
        exc = ExceptionInfo()
        dest = lib.GetAuthenticPixels(self, tx, ty, w, h, exc)
        if not dest:
            raise ImageMagickException(exc)
        src = lib.GetAuthenticPixels(source, sx, sy, w, h, exc)
        if not src:
            raise ImageMagickException(exc)
        artype = ctypes.POINTER(PixelPacket*(w*h))
        artype1 = PixelPacket*(w*h)
        dest = ctypes.cast(dest, artype)
        src = ctypes.cast(src, artype)
        for i in range(w*h):
            dest[0][i] = src[0][i]
        if not lib.SyncAuthenticPixels(self, exc):
            raise ImageMagickException(exc)

    def getPixels(self, x, y, w, h):
        return PixelWrapper(self, x, y, w, h)

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
    makeTrim = new_image_wrapper(lib.TrimImage)
    makeExtent = new_image_wrapper(lib.ExtentImage, ctypes.POINTER(RectangleInfo))
    makeBorder = new_image_wrapper(lib.BorderImage, ctypes.POINTER(RectangleInfo))

    _applyContrastStretch = apply_image_wrapper(lib.ContrastStretchImage, ctypes.c_char_p)
    applyNormalize = apply_image_wrapper(lib.NormalizeImage)
    applyComposite = apply_image_wrapper(lib.CompositeImage, CompositeOp, _PImage, ctypes.c_int, ctypes.c_int)
    _applySigmoidalContrast = apply_image_wrapper(lib.SigmoidalContrastImage, ctypes.c_int, ctypes.c_char_p)
    applySeparateChannel = apply_image_wrapper(lib.SeparateImageChannel, ChannelType)
    applyNegate = apply_image_wrapper(lib.NegateImage, ctypes.c_int)

    def applyQuantize(self, number_colors, dither=DitherMethod.No,
        colorspace=ColorspaceType.RGB, measure_error=False):
        qi = QuantizeInfo()
        qi.dither_method = dither
        qi.dither = dither != DitherMethod.No
        qi.number_colors = number_colors
        lib.QuantizeImage(qi, self)

    def applyDissolve(self, im, x=0, y=0, percent=None, dst_percent=None):
        g = im.geometry
        s = dst_percent is not None and "%fx%f" % (percent, dst_percent) or "%f" % percent
        im.geometry = s
        try:
            return self.applyComposite(CompositeOp.Dissolve, im, x, y)
        finally:
            im.geometry = g

    def applyContrastStretch(self, val):
        self._applyContrastStretch(val.encode('ascii'))

    def applySigmoidalContrast(self, a, b):
        self._applySigmoidalContrast(a, b.encode('ascii'))

    def compare(self, other, metric):
        dbl = (ctypes.c_double*1)()
        exp = ExceptionInfo()
        img = CompareImageChannels(self, other, ChannelType.All, metric, dbl, exp)
        if not img:
            raise ImageMagickException(exp)
        return (dbl[0], Image(img))

    setColorspace = apply_image_wrapper(lib.SetImageColorspace, ColorspaceType)

    def copy(self):
        exc = ExceptionInfo()
        res = lib.CloneImage(self, 0, 0, True, exc)
        if not res:
            raise ImageMagickException(exc)
        return Image(res)

    def setBackgroundColor(self, color):
        self.background_color = color
        lib.SetImageBackgroundColor(self)

    def setMatte(self, value):
        if bool(value) != bool(self.matte):
            lib.SetImageOpacity(self, OpaqueOpacity)

    def setVirtualPixelMethod(self, value):
        lib.SetImageVirtualPixelMethod(self, int(value))

CompareImageChannels = lib.CompareImageChannels
CompareImageChannels.argtypes = [_PImage, _PImage, ChannelType, MetricType, ctypes.POINTER(ctypes.c_double), ExceptionInfo]

## Constants
OpaqueOpacity = 0
TransparentOpacity = 65535

from magickpy.draw import DrawInfo #avoiding circular import
