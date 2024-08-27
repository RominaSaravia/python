from typing import Annotated
from fastapi import FastAPI,Request, Response, Cookie
from sqlmodel import Session,select,delete
from db import Product,Carts,create_db_and_tables,engine,readAllProducts,createNewProduct,deleteProduct,getCart,createCartProduct

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



templates = Jinja2Templates(directory="server/templates")
@app.get("/seeproducts", response_class=HTMLResponse)
async def read_item(request: Request,search:str=''):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"productsList": readAllProducts(search)}
    )

@app.get("/",response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>eShop</title>
        </head>
        <body>
            <h1>Welcome! Are you buying?</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/product")
def create_product(product: Product):
    return createNewProduct(product)


# @app.get("/products")
# def read_products():
#     with Session(engine) as session:
#         products = session.exec(select(Product)).all()
#         return products

#Filter by name
@app.get("/products")
async def get_products(search:str):             
    return readAllProducts(search) 

    
@app.delete("/product/{id}")
def delete_product(id:int):
    return deleteProduct(id)
    



#### ------------COOKIES---------------------

@app.post("/auth")
async def authenticate(body:dict, res:Response):
    res.set_cookie('userId',body)
    return 'Authenticated OK'



@app.get("/read_cookie")
async def get_cookie(my_var: Request):
    print(f'Cookie: {my_var._cookies}')
    return my_var._cookies


############# Carrito #################
@app.post("/cart")
async def add_to_cart(cart:Carts):
    print(f'cart creado')
    return createCartProduct(cart)


@app.get("/cart/{userId}")
async def get_cart_by_user(userId:int):
    print(f'producto agregado al carrito del usuario "{userId}" --> id producto: ', userId)
    carrito = getCart(userId)
    return carrito


