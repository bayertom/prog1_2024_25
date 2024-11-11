import sys

#Factorial code converted to the function
def factorial(n:int)->int:
    fn = 1

    while n > 1:
        fn = n * fn
        n = n - 1
        
    return fn

#Passing two parameters, v1
def calculator(a : float, b:float) ->float:
    #With local variables
    r1 = a + b
    r2 = a - b
    r3 = a * b
    
    return r1, r2, r3 

#Passing two parameters, v2
def calculator2(a : float, b:float) ->float:
    #With local variables
    return a + b, a - b, a * b 

#Immutable object
def f1(x):
    print(id(x))
    x = x + 10
    print(x)
    print(id(x))
   
#Mutable object
def f2(L):
    print(id(L))
    L[1] = 1244
    print(L)
    print(id(L))

#Comput distance, default parameter values
def distance(x1, y1, x2 = 10, y2 = 10):
    dx = x1 - x2
    dy = y1 - y2
    return (dx*dx + dy*dy)**0.5

#Passing function as a parameter, v1
def comb(n, k, f):
    #With local variables
    fn = f(n)
    fnk = f(n-k)
    fk = f(k)
    
    return fn/(fnk*fk)

#Passing function as a parameter, v2
def comb2(n, k, f):
    #Without local variables
    return f(n)/(f(n-k)*f(k))

#Without passing a function, v3
def comb3(n, k):
    return factorial(n)/(factorial(n-k)*factorial(k))
    
#Compute sum
def sum(*L):
    lsum = 0
    for l in L:
        lsum += l
    return lsum 

#Compute factorial
n = 5
res = factorial(n)
print(res)  

#Pass/return multiple parameters 
a, b = 12.0, 6.0
o1, o2, o3 = calculator(a, b) 
o4, o5, o6 = calculator2(a, b) 

print(o1, o2, o3)
print(o4, o5, o6)

#Immutable object
x = 10
print(id(x))
f1(x)
print(x)
print(id(x))

#Mutable object
L1 = [1, 2, 3]
print(id(L1))
f2(L1)
print(L1)
print(id(L1))

#Compute distance
x1, y1 = 0, 0
x2, y2 = 1, 1
d = distance(x1, y1, x2, y2) 
print(d)

#Default values, compute distance
d = distance(x1, y1) 
print(d)

#Default values have lower priority
d = distance(x1, y1, x2, y2) 
print(d)
 
#Passing function as a parameter
n = 5
k = 3
c = comb2(n, k, factorial) 
c = comb3(n, k) 

#Compute sum
L = [1, 2, 3, 4, 5]
res = sum(10, 2, 0, 30)
print(res)


#Main function
def main(args):
    n = 5
    res = factorial(n)
    print(res)  
    
#Automatic run main() function
if __name__ == '__main__':
    main(sys.argv)
 