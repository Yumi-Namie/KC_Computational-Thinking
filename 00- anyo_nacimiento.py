# Quien eres
nombre = input("Cómo te llamas?")
print("Hola, ", nombre)

#Toma de datos
edad = input("Cuantos años tienes?")
edad = int(edad)
anyo_actual = input("En qué año estamos?")
anyo_actual = int(anyo_actual)
has_cumplido = input("¿Has cumplido años ya (s/n)?")
has_cumplido = has_cumplido.lower()

#Cálculo del año
anyo_nacimiento = anyo_actual - edad

#Resultado
print(nombre, "naciste en ", anyo_nacimiento)
            
                  
                  

