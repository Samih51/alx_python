"""creation of an empty class"""
class ExcludeInitSubclassMeta(type):
    """this excludes __init_subclass__ from the output"""
    def __dir__(self):
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != "__init_subclass__"]

class BaseGeometry(metaclass=ExcludeInitSubclassMeta):
    """The empty class"""
    def area(self):
       raise NotImplementedError("area() is not implemented")

a=BaseException()
print(a.area())
