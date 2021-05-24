from Helado import claseHelado
from ManejadorSabores import claseMS
class claseMH: #clase manejador de helados
    __lhv = []   #lista de helados vendidos
    __ms = None  #manejador de sabores
    def __init__(self):
        self.__ms = claseMS()
    def mostrarSabores(self):
        self.__ms.mostrar()
    def ventaHelado(self, sabores = None, gr = 0):  #almacena la venta de un helado
        unHelado = claseHelado()
        helado = []
        for i in range(len(sabores)):
            helado.append(self.__ms.getLS()[sabores[i]-1])
        unHelado.addSabores(helado)
        unHelado.addGr(gr)
        self.__lhv.append(unHelado)
        helado.clear()
    def getLS(self):    #devuelve la lista de sabores
        return self.__ms.getLS()
    def getGrSabor(self, sabor): #obtiene los gramos vendidos de un sabor
        acum = 0
        for i in range(len(self.__lhv)):
            for j in range(len(self.__lhv[i].getSabores())):
                if(int(sabor) == self.__lhv[i].getSabores()[j].getNum()):
                    acum += round(self.__lhv[i].getGr()/len(self.__lhv[i].getSabores()))
        return acum
    def getSabores(self, gr):   #obtiene los sabores en base a los gramos del helado
        lista = []
        for i in range(len(self.__lhv)):
            if(gr == self.__lhv[i].getGr()):    #extend funciona pero repite sabores, probar con append
                for j in range(len(self.__lhv[i].getSabores())):
                    if(not(self.__lhv[i].getSabores()[j] in lista)):
                        lista.append(self.__lhv[i].getSabores()[j])
        for i in range(len(lista)):
            print(lista[i])
    def mostrarHelado(self):    #muestra las ventas realizadas
        for i in range(len(self.__lhv)):
            print('| Venta: {} |\n{}'.format(i+1, self.__lhv[i]))
            self.__lhv[i].mostrar()