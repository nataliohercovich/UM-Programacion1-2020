'''Ejercicio 2
La   pizzería   Bella   Napoli   ofrece   pizzas   vegetarianas   y   no   vegetarianas   a   sus   clientes.   Los
ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu. 
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 

Escribir   un   programa   que   pregunte   al   usuario   si   quiere   una   pizza   vegetariana   o   no,   y   en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la
pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
ingredientes que lleva.'''

class Pizzeria():

    def __init__(self):

        self.elejida = ['Mozzarella', 'Tomate']
        self.ingrediente = ' '

    def elejir(self):
        
        print ('Bienvenido')

        while True:
    
            try:

                n = input('Que tipo de pizza desea? \n 1: Vegetariana \n 2: No Vegetariana \n')
                
                if n == '1' or n == '2':
                    break
                else:
                    raise Exception
            except Exception:
                print('Elija opción 1 o 2, boludo')
        
        if n == '1':

            print('Todas las pizzas vienen con Mozzarela y Tomate, que mas desea agregare? \n -Solo un ingrediente extra- ')
            
            while True:
                try:
                    self.ingrediente = input('Opción 1 : Pimineto \nOpción 2 : Tofu')

                    if self.ingrediente == '1' or self.ingrediente == '2':
                        break
                    else:
                        raise Exception
                except Exception:
                    print('Elija opción 1 o 2')
            
            if self.ingrediente == '1':
                self.ingrediente = 'Pimiento'
            else:
                self.ingrediente = 'Tofu'

            self.elejida.append(self.ingrediente)

            print ('Su pizza es de tipo "vegetriana", con los siguientes ingredientes: ')
            print (*self.elejida)
        
        elif n == '2':
            print('Todas las pizzas vienen con Mozzarela y Tomate, que mas desea agregare? \n -Solo un ingrediente extra- ')
            
            while True:
                try:
                    self.ingrediente = input('Opción 1 : Peperoni \nOpción 2 : Jamón \nOpción 3 : Salmón')

                    if self.ingrediente == '1' or self.ingrediente == '2' or self.ingrediente == '3':
                        break
                    else:
                        raise Exception
                except Exception:
                    print('Elija opción 1, 2 o 3')
            
            if self.ingrediente == '1':
                self.ingrediente = 'Peperoni'
            elif self.ingrediente == '2':
                self.ingrediente = 'Jamón'
            else:
                self.ingrediente = 'Salmón'

            self.elejida.append(self.ingrediente)

            print ('Su pizza es de tipo "NO vegetriana", con los siguientes ingredientes: ')
            print (*self.elejida)
         

if __name__ == "__main__":
    
    pizzeria = Pizzeria()
    pizzeria.elejir()        