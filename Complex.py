import math

class Complex:

    #Complex has two fields, real and img which
    # are both integers representing the real and imaginary
    #parts of a complex number
    def __init__(self,real,img):
        self.real = real
        self.img = img


    def magnitude(self):
        radicand = self.real **2 +self.img**2
        return math.sqrt(radicand)

    #(a+bi)(a+bi) = a^2 + 2abi - b^2
    def square(self):
        result = Complex(0,0)
        result.real = self.real**2 - self.img**2
        result.img = 2*self.real*self.img
        return result

    def plus(self, other):
        self.real += other.real
        self.img += other.img
        
    def __repr__(self):
        real = "{:.2f}".format(self.real)
        img = "{:.2f}".format(self.img)
        str = (f"{real} + {img}i")
        return str