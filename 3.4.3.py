class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def midpoint(self, other):
        midX = (self.x + other.x)/2
        midY = (self.y + other.y)/2
        return Point(midX, midY)# makes a new instance here

    def addPoint(self, point):
        self.x += point.x
        self.y += point.y

    def projectToYAxis(self):
        return Point(0, self.y)

p1 = Point(3, 4)
p2 = p1.projectToYAxis()
assert(str(p2) == 'Point(x=0, y=4)')