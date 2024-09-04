'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
Erick Romo
class CuentaBancaria:

  def __init__(self,nuemroCta=None, nombreCliente=None, fechaApertura=None, saldo=None):
   self.__numeroCta=numeroCta
    self.__nombreCliente=nombreCliente
    self.__fechaApertura=fechaApertura
    self.__saldo=saldo

def get_numeroCta(self):
  return self.__numeroCta

def get_fechaApertura(self):
  return self.__fechaApertura

def get_saldo(self):
  return self.__saldo
  
  
  

