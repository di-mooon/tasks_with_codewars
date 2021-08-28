class LazyInit(type):

    def __call__(cls, *args):
        obj = type.__call__(cls, *args)
        for i, j in zip(obj.__init__.__code__.co_varnames[1:], args):
            setattr(obj, i, j)
        return obj

