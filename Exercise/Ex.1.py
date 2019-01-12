print('saifullah- 18B-092-CS, A')
print('LAB-04,  P.Ex 1')
import math
a = int(input('The value of a:'))
b = int(input('The value of b:'))
c = int(input('The value of c:'))
d = (2*a)
x1 = (-b+math.sqrt(b**2 - 4*(a)*(c)))
x2 = (-b-math.sqrt(b**2 - 4*(a)*(c)))
sol1 = (x1/d)
sol2 = (x2/2)
if d == 0:
    print('The equation cannot solve as there is zero division')
else:
    print('solution of both equations are:' ,sol1, sol2)
