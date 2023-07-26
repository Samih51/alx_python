def no_c(my_string):
    length=len(my_string)
    i=0
    while(i<length):
        if (my_string[i]=="c" | my_string[i]=="C"):
            del my_string[i]
        i+=1
    return my_string