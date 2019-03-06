#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    ano=int(input("Introduzca el año deseado: "))
    if ano % 400==0:
        print("El año es bisiesto")
    elif ano % 100==0:
        print("El año NO es bisiesto")
    elif ano % 4==0:
        print("El año es bisiesto")
   
    
if __name__ == "__main__":
    main()

