class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def transate(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other_point):
       import math
       d = math.sqrt(self.x*self.x + self.y*self.y)
       return (d)
       # return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    def __str__(self):
        return ('('+str(self.x)+','+str(self.y)+')')
        #return f"Point({self.x}, {self.y})"
    def __add__(self,p):
        return (Point(self.x + p.x, self.y + p.y))