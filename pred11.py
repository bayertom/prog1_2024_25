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

