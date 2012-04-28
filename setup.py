from setuptools import setup, find_packages

setup(
    name = "MagickPy",
    version = "0.2",
    packages = find_packages(exclude=["tests", "tests.*"]),
    test_suite = "tests.testall.alltests",

    install_requires = ['flufl.enum'],

    # metadata for upload to PyPI
    author = "Paul Colomiets",
    author_email = "paul@colomiets.name",
    description = "Python object-oriented interface for ImageMagick using ctypes",
    license = "MIT",
    keywords = "imagemagick ctypes image manipulation crop resize retouch",
    url = "http://github.com/tailhook/magickpy",
)
