def fibonacci(nth):
    if nth == 0 :
        return 0
    if nth == 1 :
        return 1
    else:
        return fibonacci(nth-1)+fibonacci(nth-2)

def lucas(nth):
    if nth == 0 :
        return 2
    elif nth == 1 :
        return 1
    else:
        return lucas(nth-1)+lucas(nth-2)

def sum_series(nth,x=0,y=1):
    if nth == 0 :
        return x
    if nth == 1 :
        return y
    else:
        return sum_series(nth-1,x,y)+sum_series(nth-2,x,y)
