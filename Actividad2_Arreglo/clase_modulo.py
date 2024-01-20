from collections import defaultdict

class ProcesarNumeros:
    def __init__(self):
        self.numeros = []

    def agregar_numero(self, numero):
        self.numeros.append(numero)

    def ordenar(self):
        self.numeros.sort()

    def contar_pares_impares(self):
        pares = 0
        impares = 0
        numeros_pares = []
        numeros_impares = []
        for num in self.numeros:
            if num % 2 == 0:
                pares += 1
                numeros_pares.append(num)
            else:
                impares += 1
                numeros_impares.append(num)
        return pares, impares, numeros_pares, numeros_impares

    def encontrar_repetidos(self):
        repetidos = defaultdict(int)
        for num in self.numeros:
            repetidos[num] += 1

        repetidos_al_menos_dos_veces = {num: conteo for num, conteo in repetidos.items() if conteo > 1}
        return repetidos_al_menos_dos_veces
