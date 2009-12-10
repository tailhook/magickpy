from setuptools import setup, find_packages

setup(
    name = "MagickPy",
    version = "0.1.4",
    packages = find_packages(exclude=["tests", "tests.*"]),
    test_suite = "tests.testall.alltests",

    install_requires = ['munepy'],

    # metadata for upload to PyPI
    author = "Paul Colomiets",
    author_email = "pc@gafol.net",
    description = "Python object-oriented interface for ImageMagick using ctypes",
    license = "MIT",
    keywords = "imagemagick ctypes image manipulation crop resize retouch",
    url = "http://www.mr-pc.kiev.ua/en/projects/MagickPy",
)
