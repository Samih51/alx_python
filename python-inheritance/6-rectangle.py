from base_geometry import BaseGeometry
"""class that takes in width and height"""
class Rectangle(BaseGeometry):
    """class that takes in width and height and validates it"""

    def __init__(self, width, height):
        self.__width=width
        self.__height=height
    
