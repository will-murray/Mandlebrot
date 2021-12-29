
from typing import Sequence
from graphics import *
from Complex import *
size = 600

class ComplexSeq:
    def __init__(self,c):
        self.sequence = []
        self.c = c
        self.in_set = False
        self.point_seq(Complex(0,0),0)
        
        self.len = len(self.sequence)

        
    def point_seq(self, z, iteration):
        
        if z.magnitude() > 2:
            self.in_set = False
            return
        elif iteration > 30:
            self.in_set = True
            return
        else:
            z = z.square()
            z.plus(self.c)
            self.sequence.append(z)
            self.point_seq(z, iteration + 1)
    
    def draw_sequence(self,win):
        for complex in self.sequence:
            p = get_plottable(complex,win)
            p.draw(win)

    def line_sequence(self):
        result = []
        idx = 0
        while(idx<len(self.sequence)-1):
            p1 = get_plottable(self.sequence[idx],size)
            p2 = get_plottable(self.sequence[idx+1],size)
            result.append(Line(p1,p2))
            idx+=1
        return result

    def get_color(self):
        if self.len > 30:
            return "black"
        elif self.len > 25:
            return "purple"
        elif self.len > 20:
            return "red"
        elif self.len > 15:
            return "orange"
        elif self.len > 10:
            return "yellow"
        elif self.len > 5:
            return "green"
        else:
            return "white"


def get_plottable(c,size):
    real = size/2 + c.real*(size/2)
    img = size/2 - c.img*(size/2)
    return Point(real,img)
    

            
