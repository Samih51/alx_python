""" this class represents a square"""
class Square:
    """ 
        defineing the size of a square for later on use
        and checks if its an integer and greater than 0
            """
    def __init__(self,size=0):
        self.__size = size
        if size<0:
            raise ValueError("size must be >= 0")
        if type(self.__size)!= int:
            raise TypeError("size must be an integer")
    