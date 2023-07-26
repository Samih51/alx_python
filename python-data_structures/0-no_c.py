def no_c(my_string):
    length=len(my_string)
    a= my_string.replace("c","")
    b= my_string.replace("C","")
    
    return b
print(no_c("chello"))