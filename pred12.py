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
        
#Inheritance
pg = Point(45, 1, 10, 10)
pg.print()