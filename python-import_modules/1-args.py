#!/usr/bin/python3
if __name__=="__main__":
    argv = ["hello" ,"world"]
    a=len(argv)
    if a==0:
        print("0 arguments.")
    else:
        i=0
        while (i<a):
            print (i,": ",argv[i])
            i+=1
