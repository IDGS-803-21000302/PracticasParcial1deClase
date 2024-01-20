from clase_modulo import ProcesarNumeros

mis_numeros = ProcesarNumeros()
cantidad = int(input("Ingrese la cantidad de números que desea ingresar: "))


for i in range(cantidad):
    num = int(input("Ingrese un número: "))
    mis_numeros.agregar_numero(num)


mis_numeros.ordenar()
pares, impares, numeros_pares,numeros_impares = mis_numeros.contar_pares_impares()
repetidos = mis_numeros.encontrar_repetidos()

print("")
print("|||||||||||||||||||  Ordenaremos los numeros de mayor a menor ||||||||||||||||||")
print("")

print("La numeros ordenados: {}".format(mis_numeros.numeros))
print("")

print("||||||||||||||||||||| Informacion de numeros pares |||||||||||||||||||||||||||||")
print("")

print("La cantidad de numeros pares es de: {}".format(pares))
print("Los numeros impres son: {}".format(numeros_pares))

print("")
print("||||||||||||||||||||| Informacion de numeros impares |||||||||||||||||||||||||||||")

print("La cantidad de numeros impares es de: {}".format(impares))
print("Los numeros impares son: {}".format(numeros_impares))

print("")
print("||||||||||||||||||||| Los numeros repetidos son  |||||||||||||||||||||||||||||")

print("")
print("Los numeros repetidos son: {}".format(repetidos))
print("")