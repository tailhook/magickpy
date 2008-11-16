import unittest
import os.path

class TestSimple(unittest.TestCase):

    def setUp(self):
        global Animation
        from magickpy import Animation
        self.samplepath = os.path.join(os.path.dirname(__file__), 'star.png')

    def testInstantiated(self):
        from magickpy import lib
        self.assertTrue(lib.IsMagickInstantiated())

    def testRead(self):
        res = Animation.read(self.samplepath)
        self.assertTrue(res)
        return res

    def testAppend(self):
        a = self.testRead()
        a.append(self.testRead()[0])

    def testSetItem(self):
        a = self.testRead()
        a.append(a[0].copy())
        a.delay(0.2)
        a[1] = a[1].makeSample(25,25)
        return a

    def testInsert(self):
        a = self.testSetItem()
        c = a[0].copy()
        c.draw("fill white polygon 10,10 20, 10 10,20")
        a.insert(1, c)
        return a

    def testDelItem(self):
        a = self.testInsert()
        del a[2]
        return a
