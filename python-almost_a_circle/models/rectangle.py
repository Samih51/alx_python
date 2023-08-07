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

    @property
    def width(self):
        """returns the value of width"""
        return self.__width
    @width.setter
    def width(self,value):
        """sets the value of width"""
        self.__width=value
    @property
    def height(self):
        """returns the value of height"""
        return self.__height
    @height.setter
    def height(self,value):
        """sets the value of height"""
        self.__height=value
    @property
    def x(self):
        """returns the value of x"""
        return self.__x
    @x.setter
    def x(self,value):
        """sets the value of x"""
        self.__x=value
    @property
    def y(self):
        """returns the value of y"""
        return self.__y
    @y.setter
    def y(self,value):
        """sets the value of y"""
        self.__y=value