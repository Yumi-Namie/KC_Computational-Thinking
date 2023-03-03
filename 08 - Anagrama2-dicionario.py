#DICIONARIO - No solo podemos hacer lista como podemos hacer dicionario.
#Podemos utilizar el diccionario xq las claves (letras) y las frecuencias (cantid.)  son iguales
#Solo nos es igual la orden.
#o se puede poner ={} all revés de dict()

def frecuencias(word):
    resultado = dict()
    for letra in word:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1
            
    return resultado

def es_anagrama_by_dict(p1,p2):
    return frecuencias(p1) == frecuencias(p2)

#otra manera más larga:
# def es_anagrama_by_dict(p1,p2)
#  fp1 = frecuencias(p1)
#  fp2 = frecuencias(p2)
#  if fp1 == fp2:
#   return true
#  else:
#   return false
