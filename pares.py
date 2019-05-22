class Numeros():
    def __init__(self):
        self.numeros_pares = 0

    def saber_si_es_par(self, num):
        mod = num % 2
        if mod > 0:
            self.numeros_pares = 0
            return self.numeros_pares
        else:
            self.numeros_pares = 1
            return self.numeros_pares
