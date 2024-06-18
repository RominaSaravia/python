from fastapi import FastAPI

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

#################
products = [
    {"id":1,
        "nombre": "mouse",
     "category": "computacion"
    },
    {"id":2,
        "nombre": "leche Tetra",
     "category": "lacteos"
     }

]

def filtrarPorCategoria(listaProductos):
    prodFiltrados = []
    for x in listaProductos:
        if (x["category"] == "lacteos"):
            prodFiltrados.append(x)
        else:
            pass
    
    return prodFiltrados

def filtrarPorId(listaProductos, _id):
    outPut = []
    for x in listaProductos:
        if (x["id"] == _id):
            outPut.append(x)
        else:
            pass
    
    return outPut




@app.post("/productos")
async def root(product:dict ):
    print("Los datos del producto son:", product)
    products.append(product)

    return {'message: Se creo producto'}

@app.get("/productos")
async def root():
    return products

@app.get("/productos/{category}")
async def root(category:str):
    print(f'Se filta por la categoria {category}')
    return filtrarPorCategoria(products)


@app.get("/producto/{id}")
async def root(id:int):
    
    return filtrarPorId(products,id)








