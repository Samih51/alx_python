"""imports the Rectangle class from base file"""
from models.rectangle import Rectangle
"""this is a class that has all the info about square"""
class Square(Rectangle):
    """this class holds all the attributes of a square"""
    def __init__(self, size, x=0, y=0, id=None):
         super().__init__(size, size, x, y, id)
         self.__size=size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

        """getter method for size"""
    @property
    def size(self):
        """returns the value of size"""
        return self.__size
    """setter method for size"""
    @size.setter
    def size(self,value):
        """sets the value of size"""
        if not (type(value)==int):
            raise TypeError("size must be an integer")
        if value<=0:
            raise ValueError("size must be > 0")
        self.__size = value
        self.width = self.__size
        self.height = self.size
    