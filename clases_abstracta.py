#De forma nativa python no toma en cuenta las clases abstractas pero si podemos forzarlo
#para trabajar con ellas al importar um modulo incluido con python
from abc import ABCMeta, abstractmethod

#Creamos nuestra clase abstracta
class Figura(metaclass=ABCMeta):

    #Creamos nuestros metodos abstractos
    @abstractmethod
    def area(self):
        pass

    #Estos con un @ son decoradores permiten ahorrar codigo
    @abstractmethod
    def perimetro(self):
        pass

#Insatanciamos nuestra clase y le decimos que herede los metodos de la clase abstracta
class Rectangulo(Figura):
    #Inicializamos nuestra clase y nustras variables
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    #Heredamos los metodos abstractos y ahora si les damos funcionalidad
    def area(self):
        return self.ancho * self.altura

    def perimetro(self):
        return (self.ancho*2)+(self.altura*2)

#Mandamos a llamar a nuestra clase y le damos sus parametros
r = Rectangulo(5,10)
#Obtenemos y mandamos a pnatalla los resultados
print(r.area())
print(r.perimetro())