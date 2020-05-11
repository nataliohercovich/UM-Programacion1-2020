'''Ejercicio 1
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al genero y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre   posterior   a   la   N   y   el   grupo   B   por   el   resto.   Escribir   un   programa   que   pregunte   al
usuario su nombre y genero, y muestre por pantalla el grupo que le corresponde.'''

class Alumnos():

    def __init__(self):

        self.genero = ' '
        self.nombre = ' '

    def grupos(self):

        A = 'ABCDEFGHIJKLM'
       

        self.nombre = input('Cual es su nombre? ').upper()

        while True:
            try:
                self.genero = input('Cual es su género? M (masculino), F (femenino): ').upper()

                if self.genero[0] != 'M' and self.genero[0] != 'F':
                    raise ValueError

                else:
                    break
            except ValueError:
                print('Ingrese una opción correcta')
        

        if self.nombre[0] in A and self.genero == 'F':

            print ('Perteneces al grupo A')

        else:
            print ('Perteneces al grupo B')

if __name__ == "__main__":

    grupo = Alumnos()
    grupo.grupos()