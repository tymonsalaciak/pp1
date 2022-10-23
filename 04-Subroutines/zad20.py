def fun_power(x,n):
    """Tip: xn =  x * xn-1"""
    xn = x * x**n-1
    return(xn)

print(fun_power(5,3))