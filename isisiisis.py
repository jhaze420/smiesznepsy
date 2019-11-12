print("Równanie M=(a+a)/b+(a/b*a)/b+1/a "
      "a,b >=0")
a=int(input('podaj wartość parametru a:'))
b=int(input('podaj wartość parametru b:'))

if a>=0   and   b>=0:
    m = (((a+a)/b)+((a/b*a)/b)+(1/a))
    print("Wynik wynosi",m)
elif a<0   or   b<0:
    print("a albo b < 0")