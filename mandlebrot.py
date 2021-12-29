from iterator import *
from graphics import *
size = 600
resolution = 0.01
def main():
    win = GraphWin("Mandle",size,size)
    grid_walk(win)
    
    win.getMouse()
    win.close()
    


def grid_walk(win):
    real = -2
    img = -2
    while real <=  2:
        while img <= 2:

            cur = Complex(real,img)
            print(cur) 
            
            seq = ComplexSeq(cur)
            if seq.in_set:
                plottable = get_plottable(cur,size)
                plottable.draw(win)
            else:
                plottable = get_plottable(cur,size)
                plottable.setFill(seq.get_color())
                plottable.draw(win)
            img += resolution
        img = -2
        
        real += resolution


def draw_axis(win):
    x_axis = Line(Point(0,size/2),Point(size,size/2))
    x_axis.draw(win)
    y_axis = Line(Point(size/2,0),Point(size/2,size))
    y_axis.draw(win)


main()