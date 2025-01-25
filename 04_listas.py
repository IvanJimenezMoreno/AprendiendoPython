### Listas ###

mi_lista = list()
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [23, 35, 62, 30, 30 ,17, 52]

print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [23, 1.76, "Iván", "Jiménez"]

print(type(mi_lista))
print(type(mi_otra_lista))

print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-2])
print(mi_otra_lista.count("Iván"))
print(mi_lista.count(30))

edad, altura, nombre, apellido = mi_otra_lista

print(nombre)

print(mi_lista + mi_otra_lista)



mi_otra_lista.append("Aniacso")
print(mi_otra_lista)

mi_otra_lista.insert(1, "Rojo")
print(mi_otra_lista)

mi_otra_lista[1] = "Verde"
print(mi_otra_lista)

mi_otra_lista.remove("Verde")
print(mi_otra_lista)

mi_lista.remove(30)
print(mi_lista)

mi_elemento_pop = mi_lista.pop(2)
print(mi_elemento_pop)
print(mi_lista)

del mi_lista[2]
print(mi_lista)

mi_nueva_lista = mi_lista.copy()

mi_lista.clear()
print(mi_lista)
mi_nueva_lista.reverse()
print(mi_nueva_lista)

mi_nueva_lista.sort()
print(mi_nueva_lista)

print(mi_nueva_lista[1:2])



#Tipado dinámico, algo que era una lista ahora es un string
mi_lista = "Hola Python"

print(mi_lista)