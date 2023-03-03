import mis_funciones

num_notas = mis_funciones.pedir_numero()
sum_notas = 0
i=0

while i < num_notas:
    valor = mis_funciones.pedir_nota_correcta()
    sum_notas += valor
    
    i +=1
    
media = sum_notas / num_notas
print("La media es: ", media)
    



