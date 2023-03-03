def nota_numerica(letra):
    """
    Pide una nota en forma de letra y devuleve su valor en nº decimal.
    Dá error si la nota no es correcta
    """
    letras = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    letra = letra.upper()
    
    while letras[puntero] != letra:
        puntero += 1
    
    return notas[puntero]

def pedir_nota_correcta():
    """
    Pide una nota en forma de letra y si es incorrecta vuleve a pedirla.
    Devuleve el valor en nº decimal.
    """
    valor = ""
    while valor == "":
        nota = input("Nota: ")
        nota = nota.upper()
        
        try:
            valor = nota_numerica(nota)
        except IndexError:
            print("Nota", nota, "incorrecta. Vuelva a introducir")
            valor = ""
            
    return valor

def pedir_numero():
    """
    Pide un valor por la pantalla. Si no es un nº entero, vuelve a pedirlo.
    Devuelve el nº entero introcido.
    """
    valor =""
    while valor == "":
        try:
            valor = int(input("Número de asignaturas: "))
        except ValueError:
            valor = ""
            print("Debe ser un nº entero. Vuelva a introducilrlo")
        if valor<0:
            valor = ""
            print("Debe ser un nº positivo, vuelva a introducirlo")
        elif valor == 0:
            valor = ""
            print("Debe ser diferente de 0, vuelva a introducirlo")
            
    return valor