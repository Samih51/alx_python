"""imports the Rectangle class from base file"""
from models.rectangle import Rectangle
"""this is a class that has all the info about square"""
class Square(Rectangle):
    """this class holds all the attributes of a square"""
    def __init__(self, size, x=0, y=0, id=None):
         super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

