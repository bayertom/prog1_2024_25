from math import *

#Recursion
def f(n):
    print("C(" + str(n)+")")
    if (n == 1):
        print("D");
    else:
        print("f(" + str(n-1) + ")")
        f(n - 1)
    print("E(" + str(n) + ")")

f(3)

#Factorial
def fact(n):
    #Non-recursive solution
    if n == 1:
        return 1
    
    #Recursive solution
    else:
        return n * fact(n-1)

#Factorial
def fact2(n):
    #Recursive solution
    if n > 1:
        return n * fact2(n-1)
    
    #Non-recursive solution
    else:
        return 1
    

def fib(n):
    #Recursive solution
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1
    
def maximum(X, l, r):
    #Find maximum
    #Non-recursive solution
    if r <= l + 1:
        return max(X[l], X[r])
    
    #Recursive solution
    else:
        #Mid index
        m = (l + r)//2
        
        #Left subset
        xl_max = maximum(X, l, m)
        
        #Right subset
        xr_max = maximum(X, m+1, r)
        
        return max(xl_max, xr_max)
    
def bSearch(X, a, l, r):
    #Find element using bisection
    #Crossed left and right index, non-recursive solution
    if (l > r):
       return -1      

    #Recursive solution
    else:
        #Mid index
        m = (l + r)//2            

        #Number a equal to mid element
        if a == X[m]:
            return m                      

        #Number in the left subset
        elif a < X[m]:
            return bSearch(X, a, l, m - 1)

        #Number in the right subset
        else:
            return bSearch(X, a, m + 1, r )
            

#Factorial 
fn = fact(4)
fn2 = fact2(4)
print(fn, fn2)

#Fibonacci
fb = fib(20)
print(fb)

#Find maximum
X = [1, 9, 3, 4, 6, -1]
xmax = maximum(X, 0, len(X) - 1)
print(xmax)

#Find element
idx = bSearch(X, 6, 0, len(X) - 1)
print(idx)