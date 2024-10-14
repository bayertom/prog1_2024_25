Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> L=[]
>>> L
[]
>>> L=[1,2,3,8,14,-9]
>>> L
[1, 2, 3, 8, 14, -9]
>>> L=[]
>>> L.append(1)
>>> L
[1]
>>> L.append(2)
>>> L
[1, 2]
>>> L.append(3)
>>> L=[
... L
...
...
...
KeyboardInterrupt
>>> L.append(8)
>>> L.append(-14)
>>> L
[1, 2, 3, 8, -14]
>>> L[0]
1
>>> L[1]
2
>>> L[2]
3
>>> L[4]
-14
>>> L[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> len(L)
5
>>> L[2]
3
>>> L[-3]
3
>>> x = L[2]
>>> x
3
>>> L[2]==L[-3]
True
>>> L.append('Monday')
>>> L
[1, 2, 3, 8, -14, 'Monday']
>>> L[5]
'Monday'
>>> L[5][2]
'n'
>>> L[0]+L[3]
9
>>> L[0]+L[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> L
[1, 2, 3, 8, -14, 'Monday']
>>> L.pop()
'Monday'
>>> L
[1, 2, 3, 8, -14]
>>> L.append(7)
>>> L.append(-2)
>>> L.append(5)
>>> L
[1, 2, 3, 8, -14, 7, -2, 5]
>>> L[0:1]
[1]
>>> L[0:2]
[1, 2]
>>> L[1:4]
[2, 3, 8]
>>> L[1:8]
[2, 3, 8, -14, 7, -2, 5]
>>> L
[1, 2, 3, 8, -14, 7, -2, 5]
>>> L[-2:-5]
[]
>>> L[:5]
[1, 2, 3, 8, -14]
>>> L[0:]
[1, 2, 3, 8, -14, 7, -2, 5]
>>> L[:]
[1, 2, 3, 8, -14, 7, -2, 5]
>>> L
[1, 2, 3, 8, -14, 7, -2, 5]
>>> L[0:5]
[1, 2, 3, 8, -14]
>>> L[0:5:2]
[1, 3, -14]
>>> L[5:0:-1]
[7, -14, 8, 3, 2]
>>> L[:,:,-1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> L[0:7:-1]
[]
>>> L[7:0:-1]
[5, -2, 7, -14, 8, 3, 2]
>>> L
[1, 2, 3, 8, -14, 7, -2, 5]
>>> L.insert(3,111)
>>> L
[1, 2, 3, 111, 8, -14, 7, -2, 5]
>>> 10 in L
False
>>> 8 in L
True
>>> L2 = [3, 4, 5]
>>> L2
[3, 4, 5]
>>> L3 = L + L2
>>> L3
[1, 2, 3, 111, 8, -14, 7, -2, 5, 3, 4, 5]
>>> L[2]=14
>>> L
[1, 2, 14, 111, 8, -14, 7, -2, 5]
>>> L[5]=2024
>>> L
[1, 2, 14, 111, 8, 2024, 7, -2, 5]
>>> L.pop()
5
>>> L
[1, 2, 14, 111, 8, 2024, 7, -2]
>>> L.pop(0)
1
>>> L
[2, 14, 111, 8, 2024, 7, -2]
>>> W = 'I love Python'
>>> W
'I love Python'
>>> W[0]
'I'
>>> W[-1]
'n'
>>> W[0:4]
'I lo'
>>> len(W)
13
>>> W[::-1]
'nohtyP evol I'
>>> L[::-1]
[-2, 7, 2024, 8, 111, 14, 2]
>>> W[-1]='N'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> W[1]='N'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> W[1]=1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> W
'I love Python'
>>> W[0]='i'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> L[::-2]
[-2, 2024, 111, 2]
>>> W[::-2]
'nhy vlI'
>>> L.print(W)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'print'
>>> print(W)
I love Python
>>> print(W*5)
I love PythonI love PythonI love PythonI love PythonI love Python
>>> print(W*-1)

>>> W[3]
'o'
>>> ord(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected string of length 1, but int found
>>> int(W[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'o'
>>> chr(125)
'}'
>>> ord('K')
75
>>> ord(W[5])
101
>>> chr(101)
'e'
>>> S=[]
>>> S.append(1)
>>> S.append(2)
>>> S.append(3)
>>> S.append(4)
>>> S.append(5)
>>> S
[1, 2, 3, 4, 5]
>>> L.pop()
-2
>>> S.pop()
5
>>> S
[1, 2, 3, 4]
>>> S.pop()
4
>>> S
[1, 2, 3]
>>> S.pop()
3
>>> S.pop()
2
>>> S.pop()
1
>>> S
[]
>>> S.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>> Q=[]
>>> S.append(1)
>>> S.append(2)
>>> S.append(3)
>>> S.append(4)
>>> S.append(5)
>>> Q=S
>>> Q
[1, 2, 3, 4, 5]
>>> Q.pop(0)
1
>>> Q
[2, 3, 4, 5]
>>> Q.pop(0)
2
>>> Q
[3, 4, 5]
>>> Q.pop(0)
3
>>> Q
[4, 5]
>>> Q.pop(0)
4
>>> Q
[5]
>>> Q.pop(0)
5
>>> Q.pop(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>> from queue import *
>>> PQ = PriorityQueue()
>>> PQ.put((1,'Monday'))
>>> PQ.put((2,'Tuesday'))
>>> PQ.put((3,'Wednesday'))
>>> PQ.put((0.1,'Friday'))
>>> PQ.get()
(0.1, 'Friday')
>>> PQ.get()
(1, 'Monday')
>>> PQ = PriorityQueue()
>>> PQ.put((0.1,7))
>>> PQ.put((2,3))
>>> PQ.put((5,35))
>>> PQ.put((2,33))
>>> PQ.put((4,26))
>>> PQ.put((0.1,9))
>>> PQ.get()
(0.1, 7)
>>> PQ.get()
(0.1, 9)
>>> PQ.get()
(2, 3)
>>> PQ.get()
(2, 33)
>>> PQ.get()
(4, 26)
>>> PQ.get()
(5, 35)
>>> PQ.get()
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> T=()
>>> T.append(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> T.append(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> T=(1,2,3,4,89,37)
>>> T
(1, 2, 3, 4, 89, 37)
>>> T[0:5:2]
(1, 3, 89)
>>> T[0]
1
>>>
>>> T[0]=6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> T.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'pop'
>>> S={1,2,3,4,5,9,11,78}
>>> S[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> 4 in S
True
>>> S2 = {3, 9, 11, 8, -9, 24}
>>> S
{1, 2, 3, 4, 5, 9, 11, 78}
>>> S2.add(2024)
>>> S2
{3, -9, 8, 9, 2024, 11, 24}
>>> S2
{3, -9, 8, 9, 2024, 11, 24}
>>> S3 = S.union(S2)
>>> S3
{1, 2, 3, 4, 5, 8, 9, 2024, 11, 78, -9, 24}
>>> S4 = S.intersection(S2)
>>> S4
{11, 9, 3}
>>> S5 = S.difference(S2)
>>> S6 = S2.difference(S)
>>> S5
{1, 2, 4, 5, 78}
>>> S6
{8, 24, 2024, -9}
>>> D={1234:['Jan','Novak',22], 5678:['Jana', 'Novotna', 21]}
>>> D
{1234: ['Jan', 'Novak', 22], 5678: ['Jana', 'Novotna', 21]}
>>> 1234 in D
True
>>> D.get(5678)
['Jana', 'Novotna', 21]
>>>