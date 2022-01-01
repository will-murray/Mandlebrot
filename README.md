# Mandlebrot
This program, with the help of graphics.py (John Zell), generates the famous mandlebrot set. A formal description of the mandlebrot set can be found at https://en.wikipedia.org/wiki/Mandelbrot_set. I might also advise watching Numberphile's video on the topic at https://www.bing.com/videos/search?q=numberphile+mandelbrot+set&docid=608033559610398598&mid=2DB715A44ADE2EC8C6E52DB715A44ADE2EC8C6E5&view=detail&FORM=VIRE
This program can:
  1. render the mandlebrot set
  2.  visualize the movement of a complex number when said number is put under the iterative function that defines the mandlebrot set
  4. renders the filled Julia set at some point which the user clicks on.

v3 notes:
   - mandlebrot.py functionality transferred to Display.py, which implements the MandlebrotWindow ADT. This new ADT makes the render more adjustable
   - MandlebrotWindow takes window size as a parameter, sets the width and height of GraphWin ADT
   - MandlebrotWindow takes span as a parameter, span sets the render distance from origon
          ex. span = 2 -> render all c in Complex such that c.real in [-2,2] and c.img in [-2,-2]. 
   - Julia set is now colored, return type for ComplexSeq.in_julia_set changed from bool to (bool, color)
