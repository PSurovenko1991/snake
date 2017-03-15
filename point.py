

class point():
    def __init__(self, x,y,sim):
        self.x = x
        self.y = y
        self.sim = sim
    def drow(self):
        print("\n"*self.x," "*self.y,self.sim)


# p = point(10,5,"*")
# p.drow()