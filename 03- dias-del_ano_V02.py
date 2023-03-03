# extraer datos del calendario
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

def es_bisiesto(year):
    if year % 4 != 0:
    #if not year % 4 == 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
     
    return True
            

#pedir datos
dia = int(input ("Dia: "))
mes = int(input ("Mes: "))
ano = int(input("Año: "))

#comprobar bisiesto
#if es_bisiesto(ano) == True:
if es_bisiesto(ano):
    dias[1] = 29
    

#contar los dias de meses anteriores
puntero = 0
contador_dias = 0

while puntero < mes - 1:
    #contador_dias = contador_dias + dias[puntero]
    contador_dias += dias [puntero]
    puntero += 1
    
contador_dias += dia

print("El dia es:", contador_dias)
    
