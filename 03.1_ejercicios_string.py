print("Concatena los String 'Treinta', 'dias', 'de', 'Python' a un solo string")
print("--------------------------------------------------------------------------")

string1 = "Treinta"
string2 = "dias"
string3 = "de"
string4 = "Python"

string_principal = string1 + " " + string2 + " " + string3 + " " + string4

print(string_principal)
print("--------------------------------------------------------------------------")

print("Ejercicios 4 y 5")
print("--------------------------------------------------------------------------")

compañia = "Coding for all"
print(compañia)
print(len(compañia))

print("--------------------------------------------------------------------------")
print("utiliza el metodo upper para convertir el string en mayusculas")
print("--------------------------------------------------------------------------")
print(compañia.upper())
print("--------------------------------------------------------------------------")
print("utiliza el metodo ulower para convertir el string en minusculas")
print("--------------------------------------------------------------------------")
print(compañia.lower())
print("--------------------------------------------------------------------------")
print("utiliza el metodo capitalize, title y swapcase para convertir el string en capitalizar")
print("--------------------------------------------------------------------------")
print(compañia.capitalize())
print(compañia.title())
print(compañia.swapcase())
print("--------------------------------------------------------------------------")
print("Recorta la primera palabra de coding for all")
print("--------------------------------------------------------------------------")
print(compañia[0:6])
print("--------------------------------------------------------------------------")
print("comprueba si la cadena contiene Coding")
print("--------------------------------------------------------------------------")
print(compañia.find("Coding"))
print(compañia.index("Coding"))
print("Coding" in compañia)
print("--------------------------------------------------------------------------")
print("reemplaza el texto 'Coding' por 'Python'")
compañia = "Python for all"
print("--------------------------------------------------------------------------")
print("Ejercicio 12")
print(compañia.replace("for all", "for everyone"))
print("--------------------------------------------------------------------------")
print("Ejercicio 13")
compañia = "Coding for all"
print(compañia.split(" "))
print("--------------------------------------------------------------------------")
print("Ejercicio 14")
compañia = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(compañia.split(","))
print("--------------------------------------------------------------------------")
print("Ejercicio 15")
compañia = "Coding for all"
print(compañia[0])
print("--------------------------------------------------------------------------")
print("Ejercicio 16")
print(compañia[-1])
print("--------------------------------------------------------------------------")
print("Ejercicio 17")
print(compañia[10])
print("--------------------------------------------------------------------------")
print("Ejercicio 18")
compañia = "Python For Everyone"
acronym = ''.join(word[0] for word in compañia.split())
print(acronym)
print("--------------------------------------------------------------------------")
print("Ejercicio 19")
compañia = "Coding For All"
acronym = "".join(word[0] for word in compañia.split())
print(acronym)
print("--------------------------------------------------------------------------")
print("Ejercicio 20,21 y 22")

print(compañia.index("C"))
print(compañia.index("F"))
print(compañia.index("l"))
print(compañia.rfind("l"))
print("--------------------------------------------------------------------------")
print("Ejercicio 23, 24 y 25")
frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.index('because'))
print(frase.rindex('because'))
print(frase[31:55])
print("--------------------------------------------------------------------------")
print("Ejercicio 28 y 29")
compañia = "Coding For All"
print(compañia.startswith("Coding"))
print(compañia.endswith("coding"))
print("--------------------------------------------------------------------------")
print("Ejercicio 30")
compañia = "  Coding For All  "

print(compañia.strip(" "))
print("--------------------------------------------------------------------------")
print("Ejercicio 31")
compañia = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(compañia)
print(" ".join(compañia))




