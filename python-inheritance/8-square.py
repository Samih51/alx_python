"""creation of an empty class"""

class BaseGeometry():

    """the empty class"""
    def __dir__(cls)->None:
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != "__init_subclass__":
                n_attributes.append(attr)
        attributes=n_attributes
        return attributes
    
    def area(self):
         raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """this validaes value"""

        if type(value)!=int:
            raise TypeError("{} must be an integer".format(name))
        if value<0 or value==0:
            raise ValueError("{} must be greater than 0".format(name))


"""class that takes in width and height"""

class Rectangle(BaseGeometry):

    """class that takes in width and height and validates it"""

    def __init__(self, width, height):
       
        self.__width = width
        self.__height = height
       
        super().integer_validator("width",self.__width)
        super().integer_validator("height",self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width,self.__height))
  
    def area(self):
        """calculates area"""
        return(self.__width*self.__height)


"""this is a class about a square"""

class Square(Rectangle):

    """this contains all the info about square"""

    def __init__(self, size):
        self.__size=size

        super().integer_validator("size",self.__size)

    def area(self):

        """this calculates the area of a square"""

        return self.__size**2