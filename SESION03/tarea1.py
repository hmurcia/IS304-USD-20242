'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor
de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones
negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
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
#getter

def get_numeroCta(self:)
                  return self.__numeroCta
  def get_nombreCliente(self):
    return self.__nombreCliente

def get_fechaApertura(self):
  return self.__fechaApertura

def get_saldo(self):
  return self.__saldo

#metodo setter

def set_numeroCta(self, numeroCta):
  self.__numeroCta=numeroCta

def set_nombreCliente(self, nombreCliente):
   self.__nombreCliente=nombreCliente

def set_fechaApertura(self, fechaApertura):
  self.__fechaApertura=fechaApertura

def set_saldo(self,saldo):
  if saldo >= 0:
    self.__saldo=saldo

else:
     print("El saldo no puede ser negativo")

#Metodo para apertura una cuenta

def apertura_cuenta(self, numeroCta, nombreCliente, fechaApertura, saldo):
  if saldo >= 100000:

    self.set_numeroCta(numeroCta)
    self.set_nombreCliente(nombreCliente)
    self.set_fechaApertura(fechaApertura)
    self.set_saldo(saldo)
    print("Cuenta aperturada satisfactoriamente")
  else:
    print("Su saldo inicial debe ser de al menos de 100,000 pesos")
    #Metodo para realizar consignaciones

def consignar(self,monto):
  if monto > 0:
    self.__saldo += monto
    print(f"Tu consignación fue exitosa. Nuevo saldo: { self.__saldo}")
  else:
    print("El monto de tu consignacion debe ser positivo")


    #Metodo para realizar retiros controlados 

    def retirar(self,monto):
      if monto > 0 and monto <= self.__saldo:
        self.__saldo -= monto
        print(f"Retiro exitoso. Su nuevo saldo: { self.__saldo}")
      elif monto > self.__saldo:
        print("Fondos insuficientes para realizar el retiro.")
      else:
        print("El monto del retiro debe ser positivo.")

#Funcion para mostrar el menú
def mostrar_menu():
  print("\n--- Menú de Operaciones Bancarias ---")
  print("1. Aperturar cuenta")
  print("2. Consignar Dinero" )
  print("3. Retirar dinero")
  print("4. Consultar Saldo")
  print("5. Salir")
  opcion= int(input("Seleccione una opción:"))
  return opcion

#Función principal 
def main():
  cuenta = none
  while = none
  while True:
    opcion = mostrar_menú()
    
    if opcion == 1:
    numeroCta = input ("Ingrese el número de su cuenta")
    nombreCliente = input ("Ingrese el número del cliente")
    fechaApertura = input ("Ingrese la fecha de apertura (dd/mm/aaaa)")
    saldo= float(input("Ingrese el saldo inicial: "))
    cuenta= cuentaBancaria()
    cuenta.apertura_cuenta(numeroCta, nombreCliente, fechaApertura, saldo)
    
elif opcion ==2
if cuenta:
  monto:float(input("Ingrese el que va a consignar: "))
  cuenta.consignar(monto)
else:
  print("Primero debe de aperturar una cuenta")

elif opcion== 4:
if cuenta:
  print(f "saldo actual: {cuenta.get_saldo()}")
else:
  print("Primero debe de aperturar una cuenta")
elif opcion == 5:
print("Gracias por utilizar nuestro servicios")
break

else:
print("Opcion no valida. Intete de nuevo")

#Ejecutar programa principal
if__name__=="__main__":
main()
  
        
  
  
  

