from Sabor import claseSabor
import csv
class claseMS:  #clase manejador de sabores
    __ls = []   #lista de sabores
    def __init__(self): #se crea la lista de sabores a partir del archivo
        band = False
        archi = open('Lista de sabores.csv')
        reader = csv.reader(archi, delimiter = ';')
        for fila in reader:
            if(band == False):
                band = True
            else:
                unSabor = claseSabor(fila[0], fila[1], fila[2])
                self.__ls.append(unSabor)
    def mostrar(self):
        for i in range(len(self.__ls)):
            print(self.__ls[i])
    def getLS(self):    #retorna la lista de sabores
        return self.__ls