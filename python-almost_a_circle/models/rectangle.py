"""imports the Base class from base file"""
from models.base import Base
"""this is a class that has all the info about rectangle"""
class Rectangle(Base):
    """this class holds all the attributes of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not (type(width)==int):
            raise TypeError("width must be an integer")
        if width<=0:
            raise ValueError("width must be > 0")
        self.__width=width
        if not (type(height)==int):
            raise TypeError("height must be an integer")
        if height<=0:
            raise ValueError("height must be > 0")
        self.__height=height
        if x<0:
            raise ValueError("x must be >= 0")
        if not (type(x)==int):
            raise TypeError("x must be an integer")
        self.__x=x
        if not (type(y)==int):
            raise TypeError("y must be an integer")
        if y<0:
            raise ValueError("y must be >= 0")
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
        if not (type(value)==int):
            raise TypeError("width must be an integer")
        if value<=0:
            raise ValueError("width must be > 0")
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
        if not (type(value)==int):
            raise TypeError("height must be an integer")
        if value<=0:
            raise ValueError("height must be > 0")
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
        if not (type(value)==int):
            raise TypeError("x must be an integer")
        if value<0:
            raise ValueError("x must be >= 0")
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
        if not (type(value)==int):
            raise TypeError("y must be an integer")
        if value<0:
            raise ValueError("y must be >= 0")
        self.__y=value
    
    def area(self):
        return (self.__height*self.__width)