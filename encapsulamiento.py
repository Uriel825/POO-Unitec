#Como tal python no necesita atributos ni metodos privados pero podemos usar algunos trucos para encapsularlos como privados
class encapsulamiento:
    __private_atri = "Este es un atributo privado"

    def __private_metod(self):
        print('Esto es un metodo privado')

    #La unica manera en la que podemos acceder a un atributo y metodo privado
    def public_atrib(self):
        return self.__private_atri

    def public_method(self):
        return self.__private_metod()

#Intentado acceder a los atributos y metodos privados
#e = encapsulamiento()
#e.__private_metod
#e.__private_atri
# Al ser privados nos arroja un error
#AttributeError: 'encapsulamiento' object has no attribute '__private_atri'

#Accediendo a los atributos y metodos privados
e = encapsulamiento()
print(e.public_atrib())
e.public_method()
#De esta manera podemos acceder sin problemas