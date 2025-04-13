class Poly:
    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)

    def __add__(self, other):
        len_diff = len(self.coeffs) - len(other.coeffs)
        if len_diff > 0:
            padded_other = [0]*len_diff + other.coeffs
            padded_self = self.coeffs
        else:
            padded_self = [0]*(-len_diff) + self.coeffs
            padded_other = other.coeffs
        
        result_coeffs = [x + y for x, y in zip(padded_self, padded_other)]
        return Poly(*result_coeffs)

    def __repr__(self):
        return f"Poly({', '.join(map(str, self.coeffs))})"

from day4 import Poly 
a = Poly(1,2,3)  #an, ...., a0 
b = Poly(1,0,1,1,2,3)
c = a+b 
print(c) #Poly ( 1,0,1, 2,4,6)

