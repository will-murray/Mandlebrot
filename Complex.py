import math

class Complex:

    def __init__(self,real,img):
        self.real = real #imaginary compenet - float multiple of i
        self.img = img #real compenent - float


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