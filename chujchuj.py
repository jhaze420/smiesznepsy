import math
print("Funkcja Kwadratowa ax^2+bx+c")
a=int(input('podaj wartość parametru a:'))
b=int(input('podaj wartość parametru b:'))
c=int(input('podaj wartość parametru c:'))
delta = (b**2-(4*a*c))
print("delta wynosi:",delta)
if delta==0:
    x0 = (-b)/(2*a)
    print("funkcja ma jedno miejsce zerowe:",x0)
elif delta >0:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print("Funkcja ma miejsca zerowe:",x1,x2)
else:
    print("delta mniejsza niz 0")
