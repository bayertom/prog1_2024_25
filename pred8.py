from math import *

def getRadius(per):
    #Common function, may cause a problem
    return per / (2 * pi)

def getRadius2(per):
    #Use a condition
    if per > 0:
        return per / (2 * pi)
    
    #Error code
    else:
        return -1
    
def getRadius3(per):
    #Raise an exception
    if per > 0:
        return per / (2 * pi)
    
    #Negative value, throw an exception
    else:
        raise ValueError('Negative perimeter', per)


def f (a, b):
    #Use a condition
    #Error code 1
    if b==0:
        return -1
    
    #Error code 2
    elif a/b < 0:
        return -2
    
    #Computation
    else:
        return sqrt(a/b)
    
def f2 (a, b):
    #Try-catch
    try:
        return sqrt(a/b)
    
    #Value b is zero
    except ZeroDivisionError:
        return -1
    
    #Fraction a/b is negative
    except ValueError:
        return -2
    
    #Other error
    except:
        return -3
    
    
def f3 (a, b):
    #Try - catch + throw exception
    #Compute
    try:
        return sqrt(a/b)
    
    #Value b is zero
    except ZeroDivisionError:
        raise ZeroDivisionError('Division by zero', b)
    
    #Fraction a/b is negative
    except ValueError:
        raise ValueError('Outside domain', a/b)
    
    #Other error
    except:
        raise Exception('Error')

def main():
    #Syntax errors
    sin(0.5)
    #Sin(0.5)
    #sin0.5

    #Runtime errors
    x = 0.1
    y = sqrt(x) 
    print(y)

    #x = -0.1
    #y = sqrt(x) 
    #print(y)
    
    #x = 1.00000000012
    #y = asin(x)

    a = 1.0
    b = 2.0
    c = a/b
    print(c)

    #b = 0
    #c = a/b
    #print(c)

    #Logical errors
    x = (1 + 2 + 3 + 4) /4
    x = 1 + 2 + 3 + 4 / 4

    #OK
    per = 10
    r = getRadius2(per)

    #Error code
    per =-10
    r = getRadius2(per)
    if (r == -1):
        print("Error")
        
    #Exception + error code
    #r = getRadius3(per)  
    # if (r == -1):
    #    print("Error") 
    
    #OK
    a = 1
    b = 0
    c = f(a, b)
    #Zero division
    if (c == -1):
        print("Zero division")
        
    #Fraction a/b is negative
    elif c == -2:
        print("Outside domain")
        
    #Other error   
    else:
        print(c)
    
    #Use list as a, f can't detect this error
    #Try catch
    b = 1
    a = [6]
    c = f2(a, b)
    
    #Zero division
    if (c == -1):
        print("Zero division")
        
    #Zero division
    elif c == -2:
        print("Outside domain")
        
    #Other error
    else:
        print(c)
    
    #Try catch + raise   
    a = -3
    b = 1
    
    #Compute
    try:  
        c = f3(a,b)
        
    #Something happend
    except ValueError as e:
        print(e)
    
main()