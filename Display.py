
from iterator import *
from graphics import *
from Complex import *

class MandlebrotWindow:

    
    def __init__(self,size,span):
        self.reso = 0.025                               #resolution
        self.win = GraphWin("Mandlebrot Set",size,size) #window
        self.span = span                                #distance rendered from origon
        self.frame_size = size                          #window size (pixels)
        self.__draw_axis()                      



    #renders the mandlebrot set, increase reso for faster runtime
    def render_set(self):
    
        real = -1*self.span
        img = -1*self.span
        while real <=  self.span:
            while img <= self.span: 
            #for each point within a distance of |span| from (0,0)
                
                
                current_point = Complex(real,img)
                
                seq = ComplexSeq(current_point,self.frame_size,self.span)
                #^create a complex sequence with respect to window size and span

                if not seq.in_set:
                    color = seq.get_color(seq.len)
                    if color != "grey" and color != "white":
                        plottable = complex_to_px(current_point,self.frame_size,self.span)
                        # plottable = get_pixel_repr(current_point,size)
                        plottable.setFill(color)
                        plottable.draw(self.win) 

                img += self.reso
            img = -1* self.span
            real += self.reso


    #renders the sequence associated with the complex number at
    #some point which the user clicks on
    def render_chain(self):
        idx = 0
        while idx < 1000:
            click_point = self.win.getMouse()
            print(f"click point = {click_point}")
            mouse_x = click_point.getX()
            mouse_y = click_point.getY()
            c = px_to_complex(Point(mouse_x,mouse_y),self.frame_size,self.span)
            print(c)
            seq = ComplexSeq(c,self.frame_size,self.span)
            seq.draw_line_sequence(self.win)
            idx+=1
            seq.undraw_line_sequence(self.win)


    #renders in a seperate window, the julia set associated with
    #the complex number which the users clicks on
    def render_julia_set(self,jreso):
    
        idx = 0
        while idx < 3: 
            
            click_point = self.win.getMouse()
            real = click_point.getX()
            img = click_point.getY()
            c = px_to_complex(Point(real,img),self.frame_size,self.span)
            win = GraphWin("Julia Set",self.frame_size,self.frame_size)

            txt = Text(Point(200,25),f"Filled Julia set for c = {c}")
            txt.draw(win)

            seq = ComplexSeq(c,self.frame_size,self.span)
            self.__display_julia_set(seq,jreso,win)

            
            


            idx+=1
        
    #private fns - only called by render_julia_set
    #displays julia set onto new window
    def __display_julia_set(self,seq,jreso,win):
        
        real = -1*self.span
        img = -1*self.span
        while real <= self.span:
            while img <= self.span:
                current_point = Complex(real,img)

                #in julia set returns a 2-tuple (Bool, color), where color is in str form
                flag = seq.in_julia_set(current_point,0)
                

                if flag[0]: #in julia set
                    plottable = complex_to_px(current_point,self.frame_size,self.span)
                    plottable.setFill(flag[1])
                    plottable.draw(win)
                else:       
                    if flag[1] != "white":  #if current point has an escape length > 5
                        plottable = complex_to_px(current_point,self.frame_size,self.span)
                        plottable.setFill(flag[1])
                        plottable.draw(win)
                img += jreso
            img = -1*self.span
            real += jreso
        
        win.getMouse()
        win.close()

    def __draw_axis(self):


        s = self.frame_size
        x_axis = Line(Point(0,s/2),Point(s,s/2))
        x_axis.setFill("grey")
        x_axis.draw(self.win)
        y_axis = Line(Point(s/2,0),Point(s/2,s))
        y_axis.setFill("grey")
        y_axis.draw(self.win)

        #mark (1,0) and (0,1) for scale
        x_hat = complex_to_px(Complex(1,0),self.frame_size,self.span)
        y_hat = complex_to_px(Complex(0,1),self.frame_size,self.span)
        x_hat.draw(self.win)
        y_hat.draw(self.win)
        #mark (-1,0) (1,0)
        x_hat = complex_to_px(Complex(-1,0),self.frame_size,self.span)
        y_hat = complex_to_px(Complex(0,-1),self.frame_size,self.span)
        x_hat.draw(self.win)
        y_hat.draw(self.win)
        



def test_MandlebrotWindow():
    display = MandlebrotWindow(600,math.pi)

    

    p1 = display.complex_to_px(Complex(math.e,0))
    p2 = display.complex_to_px(Complex( (math.pi) ,0))
    p3 = display.complex_to_px(Complex(1,1))
    

    l = [p1,p2,p3]
    cols = ["pink","green","brown"]
    idx =0
    for i in l:
        print(i)
        c= Circle(i,10)
        c.setFill(cols[idx])
        c.draw(display.win)
        idx+=1

    display.win.getMouse()
    display.win.close()
        
def main():
    display = MandlebrotWindow(700,2.3)
    display.render_set()
    display.render_julia_set(0.02)
    
main()