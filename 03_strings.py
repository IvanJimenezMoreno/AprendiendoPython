### Strings ###

mi_string = "Mi String"
mi_otro_string = "Mi otro string"

print(len(mi_string))
print(len(mi_otro_string)) 

mi_nueva_linea_string = "Este es un string\ncon un salto de línea"
print(mi_nueva_linea_string)

mi_tab_string = "\tEste es un string con un tabulador"
print(mi_tab_string)

mi_scape_string = "\\tEste es un string con un tabulador \\n y un salto de línea escapado"
print(mi_scape_string)

#Formateo

nombre, apellido, edad = "Iván", "Jiménez", 23

print("Mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))
print("Mi nombre es %s %s y tengo %d años" %(nombre, apellido, edad))
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

#Desempaquetado de caracteres
lenguage = "python"
a, b, c, d, e, f = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

lenguage_slice = lenguage[1:3]
print(lenguage_slice)

lenguage_slice = lenguage[1:]
print(lenguage_slice)

lenguage_slice = lenguage[-2]
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2]
print(lenguage_slice)

# Reversa

lenguage_reverse = lenguage[::-1]
print(lenguage_reverse)

# Funciones

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("1".isnumeric())
print(lenguage.lower())
print(lenguage.upper().isupper())