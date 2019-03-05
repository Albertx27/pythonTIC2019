#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    N = int(input("Añadir los segundos: "))
    H = int(N/3600)
    M = int((N-(H*3600))/60)
    S = int(N-((H*3600)+(M*60)))
    print(str(H)+"horas "+str(M)+"minutos "+str(S)+"segundos")
    print("{} horas {} minutos {} segundos".format(H,M,S))

if __name__ == "__main__":
    main()

