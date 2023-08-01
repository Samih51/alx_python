""" this class represents a square    """
class Square:
    """ 
        defineing the size of a square for later on use
        and checks if its an integer and greater than 0
            """
    def __init__(self,size=0):
        self.__size = size
    
    @property
    def size(self):
        """Returns the value of size. It is a getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size. It is a setter method"""
        self.__size = value
        if type(self.__size)!= int:
            raise TypeError("size must be an integer")
    
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        """Returns the value of size. It is a getter method""" 
    
    def area(self):
        """This returns the area of a square"""
        return (self.__size**2)
a=Square(10)
a.size=2
print(a.size)