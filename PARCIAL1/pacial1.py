#Keizy Cuadrado PARCIAL 1 ESTRUCTURA DE DATOS
'''Realizar un programa que permita llenar una lista, mostrando la lista con los numeros primos menores
o iguales a un numero entero dado por el usuario utilice almenos una clase que tenga encapsulamiento y que tenga sentido en el programa'''
class Primos:
    def __init__(self, limite):
        self._limite = limite  # Atributo protegido para el límite
        self._primos = []  # Lista para almacenar los números primos

    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True
        def calcular_primos(self):
        for num in range(2, self._limite + 1):
            if self.es_primo(num):
                self._primos.append(num)

    def obtener_primos(self):
        return self._primos


def main():
    try:
        limite = int(input("Ingrese un número entero positivo: "))
        if limite < 0:
            raise ValueError("El número debe ser positivo.")

        primos = Primos(limite)
        primos.calcular_primos()  # Calcular los números primos

        print(f"Números primos menores o iguales a {limite}: {primos.obtener_primos()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
