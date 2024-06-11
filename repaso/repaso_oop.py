class Sello():
    contador = 0

    def __init__(self,nombre:str,esp:str,mat:int):
        print('Nuevo Sello')
        self.nombre = nombre
        self.especialidad = esp
        self.validarMatricula(mat)

        self.matricula = mat
        self.ID = Sello.contador
        Sello.contador = Sello.contador + 1

    def getNombre(self):
        print(f'Nombre: {self.nombre}')

    def getMatricula(self):
        print(f'Matricula: {self.matricula}')

    def estampar(self):
        print(f'------\n- {self.nombre} \n- {self.matricula} \n------\n')
    
    def validarMatricula(self,n_matricula):
        if not isinstance(n_matricula,int):
            raise Exception('Matricula no es valida');

    def miMetodo(self,num1,num2):
        if num1 > num2:
            return num1
        elif num2 > num1:
            return num2


miObj = Sello("AA","Programador",123)
miObj2 = Sello("BB","Analista",213)


miObj.getNombre()
miObj2.getNombre()

miObj.getMatricula()
miObj2.getMatricula()

miObj.estampar()