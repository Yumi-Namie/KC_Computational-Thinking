#Anagrama - palabras que tienen las mismas letras pero en diferentes ordenes
#Rama - Ama / Inglaterra - integrarla
#es_anagrama(p1,p2)- Bool {t/f}

#la primera cosa es crear una función de tachar
def tacha(caracter, word):
    lword = list(word)
    lword.remove(caracter)
    return "".join(lword)
#la lista es ideal para en este caso,xq podemos modificarla...diferente de las tuplas.
#O sea, la tuple no es mutable y portanto no es posible hacer el remove

def es_anagrama(p1,p2):
    for letra in p1:
        if letra in p2:
            p2 = tacha(letra,p2)
        else:
            return False
    return p2 == ""
        
#Es importante entender que al tachar, la plavar sigue siendo lo mismo, o sea, la palabra entera...
#para transformala en una nueva palabra sin la letra tachada, hay que resiginificarla

#DICIONARIO - No solo podemos hacer lista como podemos hacer dicionario.
#Podemos utilizar el diccionario xq las claves (letras) y las frecuencias (cantid.)  son iguales
#Solo nos es igual la orden.








    
    
