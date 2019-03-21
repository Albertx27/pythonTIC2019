#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
import math
def main():
    a = float(input("Ingrese el valor de A: "))
    b = float(input("Ingrese el valor de B: "))
    c = float(input("Ingrese el valor de C: "))
    x = (b**2)-(4*a*c)
    if x<0:
	    print ("No hay solución, la raíz es negativa")
    else:
        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)
        print(x1, x2)
#Si a es equivalente a 0
    if(A!=0):
        x=(-1*B)/A;
        print("La ecuación es igual a: " +str(x))
    elif(B!=0):
        print("Esta ecuación no tiene solución.")
    else:
        print("0 es igual a 0")

if __name__ == "__main__":
    main()

