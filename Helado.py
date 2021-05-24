class claseHelado:
    __gr = 0    #gramos
    __sabores = []
    def addSabores(self, sabores):
        self.__sabores = sabores.copy()
    def __str__(self):
        return "Helado de {}gr".format(self.__gr)
    def addGr(self, gramos):
        self.__gr += gramos
    def mostrar(self):
        for i in range(len(self.__sabores)):
            print('{}'.format(self.__sabores[i]))
    def getGr(self):
        return self.__gr
    def getSabores(self):
        return self.__sabores