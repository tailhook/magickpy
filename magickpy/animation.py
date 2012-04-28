
from magickpy import lib
from magickpy.image import ImageInfo, Image
from magickpy.types import (_ExceptionInfo, ExceptionInfo,
    ImageMagickException)

__all__ = ['Animation']

class Animation(object):

    def __init__(self, inf, img):
        self.info = inf
        self.images = [img]
        while img.next:
            img = Image(img.next)
            self.images.append(img)

    @classmethod
    def read(C, file):
        if isinstance(file, str):
            inf = ImageInfo()
            inf.filename = file
            exinfo = ExceptionInfo()
            res = lib.ReadImage(inf, exinfo)
            if not res:
                raise ImageMagickException(exinfo)
            return C(inf, Image(res))
        else:
            raise NotImplementedError

    @classmethod
    def create(C, width, height, color):
        inf = ImageInfo()
        res = lib.NewMagickImage(inf, width, height, ctypes.byref(color))
        if not res:
            raise ImageMagickException(inf.exception)
        im = Image(res)
        im.setColorspace(ColorspaceType.RGB)
        im.setBackgroundColor(color)
        return C(inf, im)

    def write(self, file):
        if isinstance(file, str):
            self.images[0].filename = file
            if not lib.WriteImage(self.info, self.images[0]):
                raise ImageMagickException(self.images[0].exception)
            return True
        else:
            raise NotImplementedError

    def append(self, img):
        if img.next or img.previous:
            raise ValueError("Can't append part of animation, copy() it before appending")
        self.images[-1].next = img
        img.previous = self.images[-1]
        self.images.append(img)

    def insert(self, index, image):
        if image.next or image.previous:
            raise ValueError("Can't insert part of animation, copy() it before inserting")
        if index > 0:
            self.images[index-1].next = image
            image.previous = self.images[index-1]
        if index < len(self.images):
            self.images[index].previous = image
            image.next = self.images[index]
        self.images.insert(index, image)

    def delay(self, value, key = None):
        value = int(value * self.images[0].ticks_per_second)
        if key is None:
            for i in self.images:
                i.delay = value
        else:
            self.images[key].delay = value

    def __getitem__(self, key):
        return self.images[key]

    def __setitem__(self, key, value):
        if value.next or value.previous:
            raise ValueError("Can't insert part of animation, copy() it before inserting")
        if key > 0:
            self.images[key-1].next = value
            value.previous = self.images[key-1]
        if key < len(self.images) - 1:
            self.images[key+1].previous = value
            value.next = self.images[key+1]
        self.images[key].next = 0
        self.images[key].previous = 0
        self.images[key] = value

    def __delitem__(self, key):
        if key > 0:
            if len(self.images) > key+1:
                self.images[key-1].next = self.images[key+1]
            else:
                self.images[key-1].next = 0
        if key < len(self.images)-1:
            if key > 0:
                self.images[key+1].previous = self.images[key-1]
            else:
                self.images[key+1].previous = 0
        self.images[key].next = 0
        self.images[key].previuos = 0
        del self.images[key]

    def __len__(self):
        return len(self.images)

