# extraer datos del calendario
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

#pedir datos
dia = int(input ("Dia: "))
mes = int(input ("Mes: "))

#contar los dias de meses anteriores
puntero = 0
contador_dias = 0

while puntero < mes - 1:
    #contador_dias = contador_dias + dias[puntero]
    contador_dias += dias [puntero]
    puntero += 1
    
contador_dias += dia

print("El dia es:", contador_dias)
    
