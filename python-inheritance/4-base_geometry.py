"""meta class to remove __init_subclass__"""
class ExcludeInitSubclassMeta(type):
    """remove __init_subclass__"""
    def __dir__(cls):
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != "__init_subclass__"]

"""creation of an empty class"""
class BaseGeometry(metaclass=ExcludeInitSubclassMeta):
    """the empty class"""
    def __dir__(cls)->None:
        attributes = super().__dir__()
        n_attributes=[]
        for attr in attributes:
            if attr !="__init_subclass__":
                n_attributes.append(attr)
        attributes=n_attributes
        return attributes
    
    def area(self):
         raise Exception("area() is not implemented")