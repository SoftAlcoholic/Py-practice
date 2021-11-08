# -*- coding: utf-8 -*-
def calculo_imc(peso,estatura):
    imc = round(float(peso)/float(estatura)**2,2)    
    return imc
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imcfin = calculo_imc(peso, estatura)
print("Tu índice de masa corporal es " + str(imcfin))

            