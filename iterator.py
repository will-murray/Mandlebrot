
from graphics import *
from Complex import *

class ComplexSeq:
    def __init__(self,c,frame_size,span,origon):
        self.points = []    #point sequence
        self.lines = []     #line sequence
        self.c = c          #Complex parameter
        self.in_set = False
        

        self.frame_size = frame_size
        self.span = span
        self.origon = origon

        self.node_list = []

        
        self.__init_point_seq(Complex(0,0),0)
        self.__init_line_sequence()
        
        self.len = len(self.points)



    #this is where the majic happens!
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
            col = self.get_color(iteration)
            # if col != "white":
            #     print(f"col = {col}, z = {z}")
            return (False, col)
        elif iteration >31:
            
            return (True,"black")
            
        else:

            next = z.square()
            next.plus(self.c)
            
            return self.in_julia_set(next,iteration+1)
        
        
    #construct a list of line segments using 'points'
    def __init_line_sequence(self):
        result = []
        idx = 0
        while(idx<len(self.points)-1):
            p1 = complex_to_px(self.points[idx],self.frame_size,self.span,self.origon)
            p2 = complex_to_px(self.points[idx+1],self.frame_size,self.span,self.origon)
            result.append(Line(p1,p2))
            idx+=1
        self.l_seq = result

    def draw_line_sequence(self,win):
        node_radius = 3
        for line in self.l_seq:
            line.draw(win)
            c1 = Circle(line.getP1(),node_radius)
            c1.draw(win)
            time.sleep(0.2)
            self.node_list.append(c1)
            
            

    def undraw_line_sequence(self,win):
        for line in self.l_seq:
            line.undraw()
        for node in self.node_list:
            node.undraw()

    def get_color(self, iter):
        if iter > 30:
            return "white"
        elif iter > 25:
            return "grey"
        elif iter > 20:
            return "red"
        elif iter > 15:
            return "orange"
        # elif iter > 10:
        #     return "yellow"
        # elif iter > 8:
        #     return "green"
        # elif iter > 6:
        #     return "purple"
        else:
            return "white"

    
    

def complex_to_px(comp,frame_size,span,origon):
    std_real = comp.real - origon[0]
    std_img = comp.img - origon[1]
    i = (frame_size/2) + (std_real * (frame_size/span/2))
    j = (frame_size/2) - (std_img * (frame_size/span/2))
    return Point(i,j)

def px_to_complex(point,frame_size,span,origon):
    i = point.getX()
    j = point.getY()
    
    real = 2* (span/frame_size) * (i - (frame_size/2))
    real += origon[0]
    img =  2* (span/frame_size) * ((frame_size/2) - j)
    img += origon[1]
    
    return Complex(real,img)

def nonstandard_complex_to_px(comp,frame_size,span,origon):
    
    i = (frame_size/2) + (comp.real * (frame_size/span/2))
    j = (frame_size/2) - (comp.img * (frame_size/span/2))
    return Point(i,j)




