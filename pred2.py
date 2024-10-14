#Initial operations
>>> 5
5
>>> type(5)
<class 'int'>
>>> 5.0
5.0
>>> type(5.0)
<class 'float'>
>>> 0.001
0.001
>>> 0.000000001234
1.234e-09
>>> 5+5
10
>>> 3+3
6
>>> True
True
>>> False
False
>>> type(True)
<class 'bool'>

#Syntax errors
>>> from math import *
>>> sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'trunc'?

#Numerical problems
>>> cos(1)
0.5403023058681398
>>> acos(cos(1))
0.9999999999999999
>>> acos(cos(1))==1
False

>>> a = 1.0 + 1.0e-16 - 1.0
0.0
>>> a = 1.0e20
1e+20
>>>  a == a + 1
True

#Strings
>>> 'Hello world'
'Hello world'
>>> 'Hello world"
  File "<stdin>", line 1
    'Hello world"
    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> "Hello world"
'Hello world'
>>> 'a'
'a'

>>> 'he\nllo'
'he\nllo'
>>> print('he\nllo')
he
llo
>>> print('he\tllo')
he      llo
>>> print('he'tl'lo')
  File "<stdin>", line 1
    print('he'tl'lo')
          ^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('he \'tl \'lo')
he 'tl 'lo

#Variables
>>> a=1
>>> type(a)
<class 'int'>
>>> a : int = 1
>>> a=7.0
>>> type(a)
<class 'float'>
>>> a = 1
>>> b = 2
>>> a/b
0.5
>>> int(a/b)
0
>>> int(12/5)
2
>>> 12/5
2.4
>>> pi
3.141592653589793

#Conversions
>>> a = 5 + 6
>>> type(a)
<class 'int'>
>>> b = 3.0 * 4.0
>>> type(b)
<class 'float'>
>>> c = 3 * 4.0
>>> type(c)
<class 'float'>
>>> b = int(3.0 * 4.0)
12
>>> b = int(3.0 * 4.6)
>>> print(b)
13
>>> type(b)
<class 'int'>
>>> b = 3 * 4.6
>>> print(b)

#Other operators
13.799999999999999
>>> 2/3
0.6666666666666666
>>> 2//3
0
>>> 12//5
2
>>> 3**2
9
>>> 4**1/2
2.0
>>> 9**1/2
4.5
>>> 9**(1/2)
3.0
>>> 9**0.5
3.0
>>> -9**0.5
-3.0
>>> (-9)**(1/2)
(1.8369701987210297e-16+3j)
>>> 12//5
2
>>> 12%5
2
>>> 13%5
3
>>> 13//8
1
>>> 13//5
2

#Functions
>>> import math
>>> math.sin(1)
0.8414709848078965
>>> math.sin(pi/2)
1.0
>>> math.asin(1)
1.5707963267948966
>>> from math import *
>>> asin(0)
1.5707963267948966
>>> log(10)
2.302585092994046
>>> log10(10)
1.0
>>> exp(1)
2.718281828459045

#Input
>>> r = input()
10
>>> r = input('Input radius: ')
Input radius: 10
>>> O = 2 * pi
>>> O = 2 * pi * r
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> type(r)
<class 'str'>
>>> r= int(r)
>>> r= float(r)
>>> O = 2 * pi * r
>>> S = pi * r * r
>>> print('Obvod: ', O)
Obvod:  62.83185307179586
>>> print('Obsah: ', S)
Obsah:  314.1592653589793
>>>