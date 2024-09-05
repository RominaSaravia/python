from typing import Annotated
from starlette.responses import RedirectResponse
from fastapi import FastAPI,Request, Response, Cookie, Form
from sqlmodel import Session,select,delete
from db import Product,Carts,create_db_and_tables,engine,readAllProducts,createNewProduct,deleteProduct,getCart,upsertCartProduct,deleteCartProduct,authUser

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/login", response_class=HTMLResponse)
async def get_login(request: Request, res:Response): 
    return templates.TemplateResponse(
        request=request, name="login.html", context={}      
    )



templates = Jinja2Templates(directory="server/templates")
@app.get("/seeproducts", response_class=HTMLResponse)
async def read_item(request: Request,res:Response,search:str=''):
    userId = validateAuth(request._cookies)
    if userId == False:
        res.status_code = 401
        return 'Error: not authorize'

    return templates.TemplateResponse(
        request=request, name="index.html", context={"productsList": readAllProducts(search)}
    )

@app.get("/seecart", response_class=HTMLResponse)
async def read_item(request: Request, res:Response):
    userId = validateAuth(request._cookies)
    if userId == False:
        res.status_code = 401
        return 'Error: not authorize'
    
    return templates.TemplateResponse(
        request=request, name="cart.html", context={"cartDetails": getCart(userId)}
    )

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    userId = validateAuth(request._cookies)
    loggedUser = False;
    if userId != False:
        loggedUser = True

    return templates.TemplateResponse(
        request=request, name="home.html", context={"logged": loggedUser}
    )


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
    
#### --------------AUTH-----------------------------
def validateAuth(cookies):
    if 'cookieUserId' in cookies.keys():
        return cookies['cookieUserId']
    else:
        return False

@app.post("/login")
async def validateLogin(email: Annotated[str, Form()] ,password: Annotated[str, Form()], res:Response):
    userAuth = authUser(email, password)

    if userAuth != None :
        res.status_code = 200
        res.set_cookie('cookieUserId', userAuth)
        return 'Login exitoso'
    else:
        res.status_code = 404
        return 'Error: email or password wrong. try again'




#### ------------COOKIES----------------------------

@app.get("/auth/{userId}")
async def authenticate( res:Response, userId:int=1):
    res.set_cookie('cookieUserId',userId)
    return 'Authenticated OK'


@app.get("/read_cookie")
async def get_cookie(request: Request):
    print(f'Cookie: {request._cookies}')
    userId = validateAuth(request._cookies)
    return userId

@app.get("/delete_cookie", response_class=RedirectResponse)
async def delete_cookie()->RedirectResponse :
    redirect = app.url_path_for('get_login')
    redirectR = RedirectResponse(url='/login')
    redirectR.delete_cookie('cookieUserId')
    return redirectR


#### ------------ Carrito --------------------------
@app.post("/cart")
async def add_to_cart(cartProduct:dict, my_var: Request, res:Response):
    userId = validateAuth(my_var._cookies)
    if userId == False:
        res.status_code = 401
        return 'Error: not authorize'
    
    if(cartProduct['amount'] == 0):
        return deleteCartProduct(userId,cartProduct['product_id'])
    else:
        print(f'cart created')
        return upsertCartProduct(userId,cartProduct['product_id'],cartProduct['amount'])


@app.get("/cart")
async def get_cart_by_user(my_var: Request, res:Response):

    userId = validateAuth(my_var._cookies)
    if userId == False:
        res.status_code = 401
        return 'Error: not authorize'
    
    carrito = getCart(userId)
    return carrito


