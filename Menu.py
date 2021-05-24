from ManejadorHelados import claseMH
import re
class claseMenu:
    __funcion = None
    __mH = None #manejador de helados
    __smv = []  #sabores mas vendidos
    __menu = {}
    def __init__(self):
        self.__menu = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.punto4, 5: self.mostrar, 6: self.salir}
        self.__mH = claseMH()
        self.__smv = [0] * len(self.__mH.getLS())
    def op(self, op):
        self.__funcion = self.__menu.get(op)
        if self.__funcion:
            self.__funcion()
        else: print('ERROR: opción inválida')
    def punto1(self):
        sabores = []
        print('| Gramos del helado: 100gr - 150gr - 250gr - 500gr - 1000gr |')
        gr = int(input('Gramos: '))
        if (gr == 100 or gr == 150 or gr == 250 or gr == 500 or gr == 1000):
            self.__mH.mostrarSabores()
            print('0 -> Finalizar')
            sabor = input('Sabor: ')
            while (int(sabor) != 0):
                if (re.match('^[0-9]', sabor.lower())):
                    if(not(int(sabor) in sabores)):
                        sabores.append(int(sabor))
                        self.__smv[int(sabor)-1] += 1
                    else:
                        print('ERROR: sabor repetido')
                else:
                    print('ERROR: sabor inválido')
                sabor = input('Sabor: ')
            self.__mH.ventaHelado(sabores, gr)
        else:
            print('ERROR: gramos inválidos')
        sabores.clear()
        print('DATO: venta realizada')
        input()
    def punto2(self):   #añadir método de ordenamiento y mostrar los 5 primeros a smv
        sabores = [0]*len(self.__smv)
        for i in range(len(self.__smv)):
            sabores[i] = [i, self.__smv[i]]
        ranking = sorted(sabores, key=lambda sabor: sabor[1], reverse=True)
        print('|----RANKING DE SABORES----|')
        for i in range(5):
            print('{}° puesto: '.format(i+1),self.__mH.getLS()[ranking[i][0]])
        input()
    def punto3(self):   #cantidad de gramos vendidos por sabor
        print('|----GRAMOS VENDIDOS DE UN SABOR----|')
        self.__mH.mostrarSabores()
        sabor = input('Sabor: ')
        print('-> Gramos vendidos: {}gr'.format(self.__mH.getGrSabor(sabor)))
        input()
    def punto4(self):
        print('|---BUSCAR POR TIPO DE HELADO----|\n| Gramos del helado: 100gr - 150gr - 250gr - 500gr - 1000gr |')
        gr = int(input('Gramos: '))
        if (gr == 100 or gr == 150 or gr == 250 or gr == 500 or gr == 1000):
            self.__mH.getSabores(gr)
        else:
            print('ERROR: gramos inválidos')
        input()
    def mostrar(self):
        self.__mH.mostrarHelado()
        input()
    def salir(self):
        print('DATO: finalizando...')