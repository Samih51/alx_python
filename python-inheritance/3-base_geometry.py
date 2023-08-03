"""creation of an empty class"""
class BaseGeometry:
    """the empty class"""
    def __dir__(cls)->None:
        attributes = super().__dir__()
        n_attributes=[]
        for attr in attributes:
            if attr !="__init_subclass__":
                n_attributes.append(attr)
        attributes=n_attributes
        return attributes