# Variables

mi_variable_string = "Mi variable String"
mi_variable_int = 5
mi_variable_bool = True
mi_variable_int_a_str = str(mi_variable_int)


print(mi_variable_string)
print(mi_variable_int)
print(mi_variable_bool)
print(mi_variable_int_a_str)
print(type(mi_variable_int_a_str))
 
# Concatenaciones de variables en un print
print(mi_variable_string, mi_variable_int, mi_variable_bool)
print("Este es el valor de:",mi_variable_bool)

# Algunas funciones del sistema
print(len(mi_variable_string))

# Variables en una sola linea. No es recomendable
nombre, apellido, alias, edad = "Iván", "Jiménez", "Ivandando", 23
print("Me llamo:", nombre, apellido,". Mi edad es:", edad, ". Y mi alias es:", alias)

# Inputs

# nombre = input("¿Cuál es tu nombre? ")
# edad = input("¿Cuál es tu edad? ")

# print("Hola", nombre, "tienes", edad, "años")

# Cambiar el tipo
nombre = 23
edad = "Iván"

print("Hola", nombre, "tienes", edad, "años")

# ¿Forzamos el tipo?
direccion: str = "Mi dirección"
direccion = 5
print(type(direccion))