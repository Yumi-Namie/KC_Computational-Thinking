#hay dos maneras de usar un fichero externo(modulo)
#la primera es usando el prefijo y importando
#la otra es como está aqui, colocamos o from y quitamos o prefijo. import con * (todo)

from m_retencion3 import *

#OBTENER DATOS DE ENTRADA
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))

# OBTENER EXENCION
exencion = obtener_exencion(situacion, num_hijos)
sueldo_a_retener = sueldo - exencion
porcentaje = obtener_retencion(sueldo_a_retener)

# OBTENER RETENCION
monto_anual = sueldo_a_retener * porcentaje / 100
monto_mensual = monto_anual / 12

#MOSTRAR RESULTADOS
print("Sueldo anual: \t", sueldo)
print("Situacion:\t", situacion)
print("Base a retener:", sueldo_a_retener)
print("Porcentaje:\t", porcentaje)
print("Total anual:\t", monto_anual)
print()
print("Retencion mensual:", monto_mensual)


    

            
