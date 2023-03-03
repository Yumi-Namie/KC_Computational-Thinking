# Quien eres
nombre = input("Cómo te llamas?")
print("Hola, ", nombre)

#Toma de datos
edad = int(input("Cuantos años tienes?"))

anyo_actual = int(input("En qué año estamos?"))

has_cumplido = input("¿Has cumplido años ya (s/n)?")
has_cumplido = has_cumplido.lower()

if has_cumplido == "s":
    anyo_nacimiento = anyo_actual - edad
else:
    anyo_nacimiento = anyo_actual - edad
    anyo_nacimiento = anyo_nacimiento - 1

#Resultado
print(nombre, "naciste en ", anyo_nacimiento)
            
                  
                  

