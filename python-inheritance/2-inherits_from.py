"""This function checks if an class inherits form another class"""
def inherits_from(obj, a_class):
    """returns true/flase if its inherited or not"""
    return(issubclass(obj,a_class))