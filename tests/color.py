import unittest

class TestRGB(unittest.TestCase):

    def setUp(self):
        global Color, ImageMagickException
        from magickpy import Color, ImageMagickException

    def testRgb(self):
        c = Color.rgb(0.5, 0.5, 0.5)
        self.assertEqual('<Color: rgba(32767,32767,32767,0)>', repr(c))

    def testBlue(self):
        c = Color.named("blue")
        self.assertEqual('<Color: rgba(0,0,65535,0)>', repr(c))

    def testYellow(self):
        c = Color.named("yellow")
        self.assertEqual('<Color: rgba(65535,65535,0,0)>', repr(c))

    def testStr(self):
        c = Color.named("yellow")
        self.assertEqual('#ffff0000', str(c))

    def testUnknown(self):
        self.assertRaises(ImageMagickException, Color.named, "no_such_color")
