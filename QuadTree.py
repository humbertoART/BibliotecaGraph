class Point:
    def __init__(self, x, y, node=None):
        self.x = x
        self.y = y
        self.node = node

class Rectangle:
    def __init__(self,x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return (
            self.x - self.w/2 <= point.x <= self.x + self.w/2 and
            self.y - self.h/2 <= point.y <= self.y + self.h/2
        )
    
class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

        self.northeast = self.northwest = None
        self.southeast = self.southwest = None

        self.mass = 0
        self.mass_center_y = 0
        self.mass_center_x = 0

    def subdivide(self):
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.w/2, self.boundary.h/2
        NE = Rectangle(x + w/2, y - h/2, w, h)
        NW = Rectangle(x - w/2, y - h/2, w, h)
        SE = Rectangle(x + w/2, y + h/2, w, h)
        SW = Rectangle(x - w/2, y + h/2, w, h)

        self.northeast = QuadTree(NE, self.capacity)
        self.northwest = QuadTree(NW, self.capacity)
        self.southeast = QuadTree(SE, self.capacity)
        self.southwest = QuadTree(SW, self.capacity)

        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False
        
        self.mass += 1
        self.mass_center_x = (self.mass_center_x * (self.mass - 1) + point.x)/self.mass
        self.mass_center_y = (self.mass_center_y * (self.mass - 1) + point.y)/self.mass
        
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()
            return (
                self.northeast.insert(point) or
                self.northwest.insert(point) or
                self.southeast.insert(point) or
                self.southwest.insert(point)
            )