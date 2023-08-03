"""This function checks if an object is an instance of a class"""
def is_kind_of_class(obj, a_class):
    """returns true/false if it is an instance"""
    if type(obj)==list and a_class==list:
        return True
    if obj==None or  type(obj)==bool or type(obj)==list: 
        return False
    return(isinstance(obj,a_class))

