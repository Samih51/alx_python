"""imports the Base class from base file"""
from base import Base
"""this is a class that has all the info about rectangle"""
class Rectangle(Base):
    """this class holds all the attributes of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.id=super().id
        self.__width=width
        self.__height=height
        self.__x=x
        self.__y=y

    """getter method for width"""
    @property
    def width(self):
        """returns the value of width"""
        return self.__width
    """setter method for width"""
    @width.setter
    def width(self,value):
        """sets the value of width"""
        self.__width=value
    """getter method for height"""
    @property
    def height(self):
        """returns the value of height"""
        return self.__height
    """setter method for height"""
    @height.setter
    def height(self,value):
        """sets the value of height"""
        self.__height=value
    """getter method for x"""
    @property
    def x(self):
        """returns the value of x"""
        return self.__x
    """setter method for x"""
    @x.setter
    def x(self,value):
        """sets the value of x"""
        self.__x=value
    """getter method for y"""
    @property
    def y(self):
        """returns the value of y"""
        return self.__y
    """setter method for y"""
    @y.setter
    def y(self,value):
        """sets the value of y"""
        self.__y=value