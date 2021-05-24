from Menu import claseMenu
import re
import os
if __name__ == '__main__':
    if(input('¿Testear?: ').lower() == 'si'):
        pass
    else:
        #inicialización de variables
        band = False
        menu = claseMenu()
        #tareas
        while not band:
            print('|----MENU----|\n1. Registrar helado vendido\n2. Mostrar los más vendidos\n3. Gramos vendidos\n4. '
                  'Tipo de helado\n5. Mostrar ventas\n6. Salir')
            op = input('Opción: ')
            if (re.match('^[0-9]', op.lower())):
                os.system('cls')
                menu.op(int(op))
                band = int(op) == 6
            else:
                print('ERROR: opción inválida')
                input()