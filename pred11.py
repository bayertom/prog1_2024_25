#Class Point 2D, encapsulation
class Point2D:
    __n = 0
    
    #Inicializator
    def __init__(self, x_ = 0, y_ = 0):
        self.__x = x_
        self.__y = y_
        Point2D.__n = Point2D.__n + 1
        self.__id = Point2D.__n
        
    def print(self):
        print('Amount of points: ', Point2D.__n)
        print('id = ', self.__id, 'x = ', self.__x, ', y = ', self.__y)

    def getN():
        return Point2D.__n
    
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
        
class Algorithms:
    def dist(self, p1:Point2D, p2:Point2D)->float:
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        
        return (dx * dx + dy * dy)**0.5   
    
    def dist2(p1:Point2D, p2:Point2D)->float:
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        
        return (dx * dx + dy * dy)**0.5 
    
    def mid(self, p1:Point2D, p2:Point2D)->Point2D:   
        xm = 0.5 * (p1.x + p2.x) 
        ym = 0.5 * (p1.y + p2.y) 
        
        return Point2D(xm, ym)


class Line:
    
    def __init__(self, p1:Point2D, p2:Point2D):
        self.__s = p1
        self.__e = p2
        
    def print(self):
        print('Line:')
        self.__s.print()
        self.__e.print()
   
    @property
    def s(self):
        return self.__s#
    
    @s.setter
    def s(self, s):
        self.__s = s
        
class Polyline:
    
    def __init__(self, *points):
        self.__vertices = points
        
    def print(self):
        print('Polyline:')
        for v in self.__vertices:
            v.print()

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
        

#No direct access to data members
p5 = Point2D(5, 5)
p6 = Point2D(16, 12)

#Attribute x is not visible
#print(p5.__x)

#Object methods, getters
x5 = p5.getX()
y5 = p5.getY()
print(x5, y5)

x6 = p6.getX()
y6 = p6.getY()
print(x6, y6)

#Class methods, getter
n = Point2D.getN()
print(n)

#Object methods
p5.setX(27)
p5.setY(2025)
p5.print()

#Property
x5 = p5.x
p5.x = 237
p5.print()

#Passing objects as parameters, object methods
a = Algorithms()
d = a.dist(p5, p6)

#Passing objects as parameters, class methods
d = Algorithms.dist2(p5, p6)

print(d)

#Return new object
pm = a.mid(p5, p6)
pm.print()

#Composition, line
l = Line(p5, p6)
l.print()

#Composition, polyline
p7 = Point2D(0, 0)
p8 = Point2D(10, 10)
pl = Polyline(p5, p6, p7, p8)
pl.print()

#Inheritance
pg = Point(45, 1, 10, 10)
pg.print()