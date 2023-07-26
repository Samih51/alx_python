def no_c(my_string):
    length=len(my_string)
    a= my_string.translate({ord('c'): None})
    b= a.translate({ord('C'): None})
    return b