class Sello():
    contador = 0

    def __init__(self,nombre,esp):
        print('Nuevo Sello')
        self.nombre = nombre
        self.especialidad = esp
        self.matricula = Sello.contador
        Sello.contador = Sello.contador + 1

    def getNombre(self):
        print(f'Nombre: {self.nombre}')

    def getMatricula(self):
        print(f'Matricula: {self.matricula}')

    def estampar(self):
        print(f'------\n- {self.nombre} \n- {self.matricula} \n------\n')

    def miMetodo(self,num1,num2):
        if num1 > num2:
            return num1
        elif num2 > num1:
            return num2


miObj = Sello("AA","a")
miObj2 = Sello("BB","b")


miObj.getNombre()
miObj2.getNombre()

miObj.getMatricula()
miObj2.getMatricula()

miObj.estampar()