def es_palindromo(string):
    string = string.replace(" ", "")
    string = string.upper()
    
    return string == string[::-1]

def saca_vocales(cadena):
    resultado = ""
    for letra in cadena:
        if letra in "aeiouAEIOU":
            resultado += letra
            
    return resultado

#for significa para cada ... in (dentro)
#return é mostrar o resultado

if __name__ == "__main__":
    print(es_palindromo("Never Odd or Even"))