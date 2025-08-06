# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.
class Animal:
    def __init__(self,species):
        self.species = species
    
    def make_sound(self):
        print("grrrr")

perro = Animal("Perro")
print(perro.species)
perro.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__(self,species):
        self.species = species
    
    def make_sound(self):
        if self.species == "perro":
            print("guau")
        elif self.species == "gato":
            print("miau")
        elif self.species == "vaca":
            print("muuuu")

perro = Animal("perro")
gato = Animal("gato")
vaca = Animal("vaca")

perro.make_sound()
gato.make_sound()
vaca.make_sound()

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0
    
    def accelerate(self):
        self._speed += 10
    
    def brake(self):
        if self._speed >= 10:
            self._speed -= 10
        else:
            self._speed = 0
    
    def read_speed(self):
        print(self._speed)

# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book:
    def __init__(self, title, autor):
        self.title = title
        self._author = autor
    
    def obtiene_autor(self):
        print(self._author)
    
    def modifica_titulo(self, titulo):
        self.title = titulo

libro1 = Book("señor de los anillos", "Tolkien")

libro1.obtiene_autor()
libro1.modifica_titulo("El Señor de los Anillos")
print(libro1.title)        

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas
    
    def calcula_media(self):
        suma = 0
        for nota in self.notas:
            suma += nota
        return suma / len(self.notas)

estud1 = Estudiante("David","Tena", [9,8])
print(estud1.calcula_media())
estud1.notas.append(7)
print(estud1.calcula_media())
print(estud1.notas)

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def retirar_dinero(self, cantidad):
        if cantidad > self.balance:
            print(f"No es posible. Cantidad disponible: {self.balance}")
        else:    
            self.balance -= cantidad
    
    def ingresar_dinero(self, cantidad):
        self.balance += cantidad

cuenta_david = BankAccount("David", 200)
cuenta_david.retirar_dinero(100)
print(cuenta_david.balance)
cuenta_david.ingresar_dinero(3000)
cuenta_david.retirar_dinero(443)
print(cuenta_david.balance)
cuenta_david.retirar_dinero(3000)

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia_puntos(self):
        return self.y - self.x    

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, minuta, horas):
        self.name = name
        self.minuta = minuta
        self.horas = horas
    
    def pago_total(self):
        return self.minuta * self.horas

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self):
        self.inventory = []
    
    def añadir_producto(self, producto):
        self.inventory.append(producto)
    
    def mostrar_producto(self):
        for objeto in self.inventory:
            print(objeto)

ikea = Store()
ikea.añadir_producto("mesa")
ikea.añadir_producto("silla")
ikea.mostrar_producto()

