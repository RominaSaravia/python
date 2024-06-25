from fastapi import FastAPI
from validations import Product

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola! servidor de prueba de la clase de Esp. en desarrollo Web!"}

@app.get("/search")
async def root(busqueda:str):
    return f"La búsqueda es: '{busqueda}'"

@app.get("/saludar")
async def root(nombre:str):
    return f'Hola, {nombre}, ¿Cómo estás?. \n Este es el servidor de Bruno.'

@app.get("/obtenermayor")
async def root(num1:int, num2:int):
    numeroMayor=None
    if num1 > num2: 
        numeroMayor = num1
    elif num1 < num2:
        numeroMayor = num2
    else:
        return 'Los números son iguales.'    
    return f'El número mayor es {numeroMayor}'

@app.get("/sumar")
async def root(num1:int, num2:int):
    result=None
    result = num1 + num2
   
    return f'El resultado es: {result}'

#############-----------------------------------

products = [

]

######  Funciones  #######

def filtrarPorCategoria( listaProductos, _category):
    prodFiltrados = []
    for x in listaProductos:
        if (x.category == _category):
            prodFiltrados.append(x)
    
    return prodFiltrados

def filtrarPorId(listaProductos, _id):
    for x in listaProductos:
        if (x.id == _id):
            return x
        else:
            pass


def validarId(listaProductos, _id):
    for p in listaProductos:
        if p.id == _id:
            return False
    
    return True


#### Queries ####

@app.post("/productos")
async def root(newProduct:Product ):
    if(validarId(products, newProduct.id)):
        products.append(newProduct)
        return {'message: Se creo producto'}
    else:
        return {'message: ID no valido'}

    

@app.get("/productos")
async def root() -> list[Product]:
    return products

@app.get("/productos/{_category}")
async def root(_category:str) -> list[Product]:
    return filtrarPorCategoria(products, _category)


@app.get("/producto/{id}")
async def root(id:int) -> Product:
    return filtrarPorId(products,id)


        











