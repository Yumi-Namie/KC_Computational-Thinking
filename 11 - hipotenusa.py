import math

def hipotenusa(c1, c2):
    h = math.sqrt(c1*c1 + c2*c2)
    
    return h

cateto1 = 3
cateto2 = 4

_hipotenusa = hipotenusa(cateto1, cateto2)
