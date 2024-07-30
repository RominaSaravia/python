class Vehiculo():
    def __init__(self,color:str, patente:str, velocidad:int):
        self.color = color
        self.patente = patente
        self.velocidad = velocidad
    
    def getColor(self):
        return self.color

    def calcularTiempoLlegada(self,distanciakm):
        resultado = distanciakm / self.velocidad
        return resultado


vehiulo1 = Vehiculo("negro","ERT143",100)
vehiulo2 = Vehiculo("blanco","EGH163",120)
vehiulo3 = Vehiculo("rojo","EJU908",100)
vehiulo4 = Vehiculo("azul","KRT153",80)
vehiulo5 = Vehiculo("verde","JRT149",90)

print(vehiulo1.getColor())
print(vehiulo2.getColor())
print(vehiulo3.calcularTiempoLlegada(1000))
print(vehiulo5.calcularTiempoLlegada(1000))