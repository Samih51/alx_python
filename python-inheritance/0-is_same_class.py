"""This function checks if an object is an instance of a class"""
def is_same_class(obj, a_class):
    """returns true/false if it is an instance"""
    if obj==None or obj==True: 
        return False
    return(isinstance(obj,a_class))