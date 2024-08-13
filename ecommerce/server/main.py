from typing import Annotated
from fastapi import FastAPI,Request, Response, Cookie
from fastapi.responses import HTMLResponse

app = FastAPI()

productsList = [{'name':'teclado','price':15550,'img':''}]

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

@app.get("/products")
async def getProducts():
    return productsList


@app.post("/product")
async def postProduct(productData: dict):
    print('producto creado: ', productData)
    productsList.append(productData)
    return productsList
