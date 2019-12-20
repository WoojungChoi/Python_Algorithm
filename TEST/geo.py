class point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

class line:
    def __init__(self):
        self.p1 = point(None, None, None)
        self.p2 = point(None, None, None)

x_value = [2,4,6,6,5,3,1]
y_value = [2,1,2,5,6,6,5]
c_value = ['A','B','C','D','E','F','G']