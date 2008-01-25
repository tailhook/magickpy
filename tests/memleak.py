import unittest
import os.path

class TestDestructors(unittest.TestCase):

    def setUp(self):
        global Image, ExceptionInfo, ImageInfo, DrawInfo, Color
        from magickpy import Image, ExceptionInfo, ImageInfo, Color
        from magickpy.draw import DrawInfo
        import os
        self.mult = int(os.environ.get('LEAKTEST_ITERATIONS', 1))

    def testImage(self):
        for i in range(1*self.mult):
            im = []
            for j in range(10):
                im.append(Image.create(1024, 1024, Color.named("white")))

    def testExceptionInfo(self):
        for i in range(100*self.mult):
            l = []
            for j in range(1000):
                l.append(ExceptionInfo())

    def testDrawInfo(self):
        for i in range(100*self.mult):
            l = []
            for j in range(1000):
                l.append(DrawInfo())

    def testImageInfo(self):
        for i in range(100*self.mult):
            l = []
            for j in range(1000):
                l.append(ImageInfo())

class TestDraw(unittest.TestCase):

    def setUp(self):
        global Image, Color, CompositeOp
        from magickpy import Image, Color, CompositeOp

    def testDraw(self):
        w, h, path = 68, 72, 'polygon 14,12 64,0 68,72 0,54'
        l = []
        for i in range(10):
            im = Image.create(w, h, Color.named("blue"))
            im.draw(path)
            l.append(im)
