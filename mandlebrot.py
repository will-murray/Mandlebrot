
from iterator import *
from graphics import *
import time

size = 600



# Change these resolutions if drawing speed is an issue

#########################

resolution = 0.015   #defines resolution of mandlebrot set

jreso = 0.01         #defines resolition of julia set

########################

def main():
    sequence_mode()
    
def julia_mode():
    win = GraphWin("Julia Mode",size,size)
    render_set_optimized(win,resolution)
    render_julia_set()
    win.close()

def sequence_mode():
    win = GraphWin("Julia Mode",size,size)
    render_set_optimized(win,resolution)
    render_chain(win)
    win.close()
    
    
    

def render_chain(win):
    draw_axis(win)
    prompt = Text(Point(size/2+220,size/2+200), "Click any point")
    prompt.draw(win)
    idx = 0
    while idx < 1000:
        click_point = win.getMouse()
        prompt.undraw()
        mouse_x = click_point.getX()
        mouse_y = click_point.getY()
        c = get_complex_repr(Point(mouse_x,mouse_y),size)
        seq = ComplexSeq(c)
        seq.draw_line_sequence(win)
        idx+=1
        seq.undraw_line_sequence(win)

def render_set(win,resolution):
    count = 0
    real = -3
    img = -3
    while real <=  3:
        while img <= 3:

            
            cur = Complex(real,img)
            
            
            seq = ComplexSeq(cur)
            if seq.in_set:
                plottable = get_pixel_repr(cur,size)
                plottable.draw(win)
            else:
                color = seq.get_color(seq.len)
                if color != "white":
                    plottable = get_pixel_repr(cur,size)
                    plottable.setFill(color)
                    plottable.draw(win)
            

            img += resolution
            count += 1
        img = -2
        
        
        real += resolution
    


#Only colors the points which are on the border of the set
def render_set_optimized(win,resolution):
    count = 0
    real = -2
    img = -2
    while real <=  2:
        while img <= 2:

            
            current_point = Complex(real,img)
            
            seq = ComplexSeq(current_point)
            if not seq.in_set:
                color = seq.get_color(seq.len)
                if color != "grey" and color != "white":
                    plottable = get_pixel_repr(current_point,size)
                    plottable.setFill(color)
                    plottable.draw(win) 

            img += resolution
            count += 1
        img = -2
        
        
        real += resolution
    
def render_julia_set():
    
    idx = 0
    while idx < 3: 
        win = GraphWin("Julia Set",size,size)
        draw_axis(win)
        click_point = win.getMouse()
        real = click_point.getX()
        img = click_point.getY()
        c = get_complex_repr(Point(real,img),size)
        
        seq = ComplexSeq(c)
        display_julia_set(seq,jreso,win)

        



        idx+=1
        
#given the Complex Sequence of c, render its associated Julia Set
def display_julia_set(seq,jreso,win):
    
    
    
    
    real = -2
    img = -2
    while real <= 2:
        while img <= 2:
            current_point = Complex(real,img)
            flag = seq.in_julia_set(current_point,0)

            if flag:
                plottable = get_pixel_repr(current_point,size)
                plottable.draw(win)
            img += jreso
        img = -2
        real += jreso
    time.sleep(2)
    win.close()





def draw_axis(win):
    x_axis = Line(Point(0,size/2),Point(size,size/2))
    x_axis.draw(win)
    y_axis = Line(Point(size/2,0),Point(size/2,size))
    y_axis.draw(win)


main()