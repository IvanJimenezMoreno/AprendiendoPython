### Operadores aritmeticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Modulo o residuo: es el resto de la división
print(10 // 3) # Division que redondea
print(3 ** 4) # Potencia
print(3 ** 4 + 3 - 7 / 1 // 4) 

print("Hola " + "Python")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

mi_float = 2.5 * 2
print("Hola " * int(mi_float))


### Operadores comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Comparación afabética por orden de la tabla ASCII

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >="Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores lógicos ###

print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python") 
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4==4))   
print(not(3 > 4)) 