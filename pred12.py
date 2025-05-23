from abc import ABC, abstractmethod
from copy import deepcopy

class GO:
    def __init__(self, color, style):
        self.__color = color
        self.__style = style
        
    def print(self):
        print(self.__color)
        print(self.__style)
        
class Point(GO):
    __n = 0
    
    #Inicializator
    def __init__(self, color, style, x_ = 0, y_ = 0):
        super().__init__(color, style)
        self.__x = x_
        self.__y = y_
        Point.__n = Point.__n + 1
        self.__id = Point.__n
        
    def print(self):
        print('Amount of points: ', Point.__n)
        print('id = ', self.__id, 'x = ', self.__x, ', y = ', self.__y)

    def getN():
        return Point.__n
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y 
    
    @property  
    def x(self):
        return self.__x
    
    @property  
    def y(self):
        return self.__y        
    
    @x.setter
    def x(self, x):
        self.__x = x
        
    @y.setter
    def y(self, y):
        self.__y = y
        
    def __lt__(self, other):
        return self.__x < other.__x 
    
    
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
'''
class Point2:
    __n = 0
    
    #Inicializator
    def __init__(self, x_ = 0, y_ = 0):
        self.__x = x_
        self.__y = y_
        Point.__n = Point.__n + 1
        self.__id = Point.__n
        
    def print(self):
        print('Amount of points: ', Point.__n)
        print('id = ', self.__id, 'x = ', self.__x, ', y = ', self.__y)
 
class PointG(GO, Point2):
    __n = 0
    
    #Inicializator
    def __init__(self, color, style, x_ = 0, y_ = 0):
        super().__init__(color, style)
            
    def print(self):
        print('Amount of points: ', Point.__n)
        print('id = ', self.__id, 'x = ', self.__x, ', y = ', self.__y)
'''
 
class Line(GO):
    
    def __init__(self, color:int, style:int, p1:Point, p2:Point):
        super().__init__(color, style)
        self.__s = p1
        self.__e = p2
        
    def print(self):
        print('Line:')
        super().print()
        self.__s.print()
        self.__e.print()
   
    @property
    def s(self):
        return self.__s#
    
    @s.setter
    def s(self, s):
        self.__s = s 

class GOA(ABC):
    def __init__(self, color, style):
        self.__color = color
        self.__style = style
    
  
    def print(self):
        print(self.__color)
        print(self.__style)   
        
    @abstractmethod              
    def print2(self):
        pass

class LineA(GOA):
    
    def __init__(self, color:int, style:int, p1:Point, p2:Point):
        super().__init__(color, style)
        self.__s = p1
        self.__e = p2
    '''   
    def print(self):
        print('Line:')
        super().print()
        self.__s.print()
        self.__e.print()
    '''
    def print2(self):
        print('Line:')
        print(super().__color)
        print(super().__style)
        self.__s.print()
        self.__e.print()
   
    @property
    def s(self):
        return self.__s#
    
    @s.setter
    def s(self, s):
        self.__s = s 


#New point
color = 45
style = 1
pg = Point(color, style, 10, 10)
pg.print()

#New Line
p1 = Point(color, style, 0, 0)
p2 = Point(color, style, 10, 10)
l = Line(128, style, p1, p2)
l.print()

#Abstract class
g = GO(color, style)

#g2 = GOA(color, style)
l = LineA(128, style, p1, p2)
#l.print()
#l.print2()

GOL = []
GOL.append(p1)
GOL.append(l)

for go in GOL:
    go.print()

GOL.append(1)

#for go in GOL:
#    go.print()

#Shallow copy
print(id(l))
l2 = l
print(id(l2))

p1 = Point(10,10)
p2 = p1
p1.x = 37
p1.print()
p2.print()
p3 = deepcopy(p1)
p1.y = 77;
p1.print()
p3.print()
print(id(p1))
print(id(p3))
