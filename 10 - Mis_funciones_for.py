import mis_funciones

num_notas = mis_funciones.pedir_numero()
sum_notas = 0

for i in range(num_notas):
    print (i)
    valor = mis_funciones.pedir_nota_correcta()
    
    sum_notas += valor

if num_notas == 0 or num_notas<0 :
    print("No se han introducido datos correctos")
else:
    media = sum_notas / num_notas
    print("La media es: ", media)
    
    
    