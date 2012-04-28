
__all__ = [
    'wrap_enum_class',
    'wrap_ptr_class',
    ]

import ctypes

def enum_as_param(self):
    return int(self)

@classmethod
def enum_from_param(C, value):
    return int(value)

def wrap_enum_class(enum):
    """Adds methods to munepy.Enum subclass to have ability to use class as
    ctypes argument
    """
    enum._as_param_ = property(enum_as_param) #hacks
    enum.from_param = enum_from_param

def wrap_ptr_class(struct, constructor, destructor, classname=None):
    """Creates wrapper class for pointer to struct class which appropriately
    acquires and releases memory
    """

    class WrapperClass(ctypes.c_void_p):

        def __init__(self, val=None):
            if val:
                super(WrapperClass, self).__init__(val)
            else:
                super(WrapperClass, self).__init__(constructor())

        def __del__(self):
            destructor(self)
            self.value = None

        def __getattr__(self, name):
            return getattr(ctypes.cast(self.value,
                                       ctypes.POINTER(struct)).contents, name)

        def __setattr__(self, name, value):
            if name == 'value' or name.startswith('_'):
                super(WrapperClass, self).__setattr__(name, value)
            else:
                cont = ctypes.cast(self.value, ctypes.POINTER(struct)).contents
                if isinstance(value, str):
                    value = value.encode('utf-8')
                setattr(cont, name, value)

    WrapperClass.__name__ = classname or struct.__name__.lstrip('_')
    return WrapperClass

