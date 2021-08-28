import inspect


class Function:

    def __init__(self, f, df):
        self.f = f
        self.df = df

    def __call__(self, *args, **kwargs):
        return self.df(*args) if kwargs.get('grad') else self.f(*args)

    def __add__(self, other):
        return self.__call__(self) + other.__call__()


#
# def __sub__(self, other):
#     return
#
# def __getitem__(self, index):
#     return
#
# def __mul__(self, other):
#     return
#
# __rmul__ = __mul__

# def __str__(self):
#     return self.df if self.grad else self.f

print(inspect.getsource(lambda x:x))

f = Function(lambda x: x ** 2, lambda x: 2 * x)
f2 = Function(lambda x: 1, lambda x: 0)
f3 = f + f2
f3(1)


