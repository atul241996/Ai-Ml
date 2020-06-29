class Point:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
    def draw(self):
        print("Point drawn")
    def move(self,y,x):
        print(f"Move {x} {y}")


p = Point(6,5)
p.draw()
p.move(x=6,y=5)



