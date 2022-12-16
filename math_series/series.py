
'''
This function takes one parameter
    and returns the nth value in the fibonacci series.
'''
def fibonacci(n):
    if type(n)!= int:
        return "please insert only numbers"
    elif n<0:
        return "please insert positive numbers"   
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

''' 
This function takes one parameter and returns the nth value in the lucas series
'''
def lucas(n):
    if type(n)!= int:
        return "please insert only numbers"
    elif n<0:
        return "please insert positive numbers"   
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

'''
that takes one parameter(n) and two optional parameters(n1,n2);
    if the user inserts only one parameter the function will call fibonacci(n)
    else if the user inserts three parameter3 and n1=2 and n2=1 the function will call lucas(n)
    else if the user inserts other values for the optional parameters it will produce other series.
'''
def sum_series(n,n1=0,n2=1):
    if type(n)!= int or type(n1)!= int or type(n2)!= int:
        return "please insert only numbers"
    elif n<0:
        return "please insert positive numbers" 
    elif n1==0 and n2==1:
        return fibonacci(n)
    elif n1==2 and n2==1:
        return lucas(n)
    else:
        if n==0:
            return n1
        elif n==1:
            return n2
        else:
            return sum_series(n-1,n1,n2)+sum_series(n-2,n1,n2)

