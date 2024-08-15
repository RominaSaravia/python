from typing import Annotated
from fastapi import FastAPI,Request, Response, Cookie
from fastapi.responses import HTMLResponse
from sqlmodel import Session,select,delete
from db import Product,create_db_and_tables,engine


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


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
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


# @app.get("/products")
# def read_products():
#     with Session(engine) as session:
#         products = session.exec(select(Product)).all()
#         return products

#Filter by name
@app.get("/products")
async def get_products(search:str):
    with Session(engine) as session:
        products = None
        if(search != None):
            products = session.exec(select(Product).where(Product.name.like('%'+ search + '%'))).all()
        else:
            products = session.exec(select(Product)).all()
                
        return products

    
@app.delete("/product/{id}")
def delete_product(id:int):
    with Session(engine) as session:
        result = session.exec(delete(Product).where(Product.id == id))
        session.commit()
        return result
    



#### ------------COOKIES---------------------

@app.post("/auth")
async def authenticate(body:dict, res:Response):
    res.set_cookie('userId',body)
    return 'Authenticated OK'



@app.get("/read_cookie")
async def get_cookie(my_var: Request):
    print(f'Cookie: {my_var._cookies}')
    return my_var._cookies


