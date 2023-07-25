#!/usr/bin/python3
if __name__=="__main__":
    from sys import argv
    a=len(argv)
    if a==1:
        print("0 arguments.")
    else:
        i=1

        while (i<a):
           
            print ("{}: {}".format(i,argv[i]))
            i+=1
