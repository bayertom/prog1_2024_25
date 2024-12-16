#Class Point 2D
class Point2D:
    n = 0
    
    def __init__(self, x_ = 0, y_ = 0):
        #Inicializator
        self.x = x_
        self.y = y_
        Point2D.n = Point2D.n + 1
        self.id = Point2D.n
        
    def print(self):
        #Method of the instance
        print('Amount of points: ', Point2D.n)
        print('id = ', self.id, 'x = ', self.x, ', y = ', self.y)

    def getN():
        #Class method
        return Point2D.n

#Create new points  + instance methods    
p1 = Point2D(10, 10)
p1.print()

p2 = Point2D(0, 10)
p2.print()

p3 = Point2D(10, 0)
p3.print()

p4 = Point2D()
p4.print()

#All points indicate same amount of n
p1.print()
p2.print()

#Class method
n = Point2D.getN()

#Direct access to data members
print(p1.x)
print(p2.y)

#Data member can be modified, no encapsulation
p1.x = 265
p1.print()

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
        print('id = ', self.id, 'x = ', self.x, ', y = ', self.y)

    def getN():
        return Point2D.__n

#No direct access to data members
p5 = Point2D(5, 5)

#Attribute x is not visible
print(p5.__x)

