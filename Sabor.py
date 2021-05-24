class claseSabor:
    __num = 0  # número
    __nom = ''  # nombre del sabor
    __des = ''  # descripción del sabor
    def __init__(self, num='0', nom='-', des='-'):
        self.__num = int(num)
        self.__nom = nom
        self.__des = des
    def __str__(self):
        formato = """{:2} -> {:25} ({})"""
        return formato.format(self.__num, self.__nom, self.__des)
    def getNum(self):
        return self.__num