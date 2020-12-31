def main():
    for i in inclusive_range(1,3):
        print(i,end ='')
    print()
    
def inclusive_range(*args):
    numargs = len(args)
    start=0
    step=1
    


    #intialize the parameters
    if numargs<1:
        raise TypeError(f'expected at least 1 arguement{numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start,stop) = args
    elif numargs == 3:
        (start,stop,step) = args
    else:
        raise TypeError(f'Atleast 3 arguements{numargs} required')


    #generator
    i = start
    while i<=stop:
        yield i
        i = i + 1

if __name__== "__main__":
    main()
    
