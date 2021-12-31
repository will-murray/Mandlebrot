
from graphics import *
from Complex import *
size = 600

class ComplexSeq:
    def __init__(self,c):
        self.points = []    #point sequence
        self.lines = []     #line sequence
        self.c = c          #Complex parameter
        self.in_set = False 

        self.node_list = []


        
        self.__init_point_seq(Complex(0,0),0)
        self.__init_line_sequence()
        #the 2 instance methods used above are private and only called in this fns
        self.len = len(self.points)

    #-----------------------------------------------
    #this is where the majic happens! #See https://en.wikipedia.org/wiki/Mandelbrot_set

    #function iterates a Complex number 'z' through the function f(z) = z^2 +c
    #for each iteration, the new value is appended to the 'points' list
    
    def __init_point_seq(self, z, iteration):
        
        if z.magnitude() > 10: #diverge to infinity
            self.in_set = False
            return
        elif iteration > 31: #converging or repeting sequence
            self.in_set = True
            return
        else:               #update and add the new z to 'points'
            z = z.square()
            z.plus(self.c)
            self.points.append(z)
            self.__init_point_seq(z, iteration + 1)
    

    def in_julia_set(self,z, iteration):
        
        if z.magnitude() > 2:
            
            return False#self.get_color(iteration)
        elif iteration >31:
            
            return True#self.get_color(iteration)
            
        else:

            next = z.square()
            next.plus(self.c)
            
            return self.in_julia_set(next,iteration+1)
        
        
    #construct a list of line segments using 'points'
    def __init_line_sequence(self):
        result = []
        idx = 0
        while(idx<len(self.points)-1):
            p1 = get_pixel_repr(self.points[idx],size)
            p2 = get_pixel_repr(self.points[idx+1],size)
            result.append(Line(p1,p2))
            idx+=1
        self.l_seq = result

    def draw_line_sequence(self,win):
        node_radius = 3
        for line in self.l_seq:
            line.draw(win)
            c1 = Circle(line.getP1(),node_radius)
            c1.draw(win)
            
            self.node_list.append(c1)
            
            

    def undraw_line_sequence(self,win):
        for line in self.l_seq:
            line.undraw()
        for node in self.node_list:
            node.undraw()

    def get_color(self, iter):
        if self.len > 30:
            return "white"
        elif iter > 25:
            return "grey"
        elif iter > 20:
            return "red"
        elif iter > 15:
            return "orange"
        elif iter > 10:
            return "yellow"
        elif iter > 8:
            return "green"
        elif iter > 5:
            return "purple"
        else:
            return "white"

    
    


#given a point 'p' with pixel coordinates
#return the complex number equivalent
def get_complex_repr(p,size):
    real = p.x/(size/2) - 1
    img = 1- p.y/(size/2)
    
    return Complex(real,img)


#given a complex number 'c' return 
#the pixel coordinate equivalent
def get_pixel_repr(c,size):
    real = size/2 + c.real*(size/2)
    img = size/2 - c.img*(size/2)
    return Point(real,img)
    


def main():

    seq = ComplexSeq(Complex(0,0))
    c = seq.in_julia_set(Complex(1,0),0)
    print(c)
    
main()

