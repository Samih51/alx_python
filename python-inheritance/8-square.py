"""meta class to remove __init_subclass__"""


class ExcludeInitSubclassMeta(type):

    """remove __init_subclass__"""
    
    def __dir__(cls):
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != "__init_subclass__"]

"""creation of an empty class"""


class BaseGeometry(metaclass=ExcludeInitSubclassMeta):

    """The base class"""

    def __dir__(cls) -> None:
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != "__init_subclass__":
                n_attributes.append(attr)
        attributes = n_attributes
        return attributes

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))

"""This is a rectangle class"""


class Rectangle(BaseGeometry):
    """Class that takes in width and height and validates it"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

"""this is a square class"""


class Square(Rectangle,metaclass=ExcludeInitSubclassMeta):
    """This class contains all the info about a square"""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """Calculates the area of a square"""
        return self.__size**2
