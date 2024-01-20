class Piramide:
    def __init__(self, n):
        self.n = n

    def imprimir_piramide(self):
        for i in range(0, self.n + 1):
            print('*' * i)

n = int(input("Digite un numero: "))

pyramid = Piramide(n)
pyramid.imprimir_piramide()

