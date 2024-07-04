from typing import Annotated
from fastapi import FastAPI,Request, Response, Cookie
from fastapi.responses import HTMLResponse
from validations import Ticket,Passenger,Flight,Code_Country,User_Credntial
from controller import filterById,auth_user

app = FastAPI()

ListTickets = [
    Ticket(
        id = 1,
        p = Passenger( id_document=48651567,name="Martha",surname="Smith",email="martha.smith@gmail.com",birth_date="12/01/2024"),
        f = Flight( destination = "ARG",origin="BRA",takeoff_date="12/01/2024")
    )
]

credentials = {
    #user:password
    'romina@gmail.com':'123456',
    'martha.smith@gmail.com':'martha123',
    'admin':'admin123'
}



@app.get("/",response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

#-------------TICKETS----------------------

@app.post("/ticket") # Buy Ticket
async def post_tickets(ticket:Ticket, req: Request, res:Response):
    ##Verify loggedUser
    user_logged = auth_user(req)
    if (user_logged != None):
        #Continue with purchase
        ListTickets.append(ticket)
        return {'message: Se creo producto'}
    else:
        #Indicate to log first
        res.status_code = 401
        return {'message: Necesita estar logeado'}  
    

@app.get("/ticket")
async def get_tickets():
    return ListTickets

@app.get("/ticket/{id}")
async def get_ticket_byId(id:int):
    return filterById(id,ListTickets)


@app.patch("/ticket/{id}")
async def patch_ticket(id:int,ti:Ticket):
    selected = Ticket
    for x in ListTickets:
        if x.id == id:
            selected = x
            index = ListTickets.index(selected)
            ListTickets[index] = ti
            return {"message": "Ticket updated"}
        
    return {"message": "NOT FOUND"}


@app.delete("/ticket/{id}")
async def delete_ticket(id:int,ti:Ticket):
    for x in ListTickets:
        if x.id == id:
            selected = x
            ListTickets.remove(selected)
            return {"message": "Ticket deleted"}
        
    return {"message": "NOT FOUND"}



#### ------------COOKIES---------------------

@app.get("/set_cookie")
async def post_cookie(res: Response):
    res.set_cookie('my_cookie','COOKIE')
    return 'Cookie generada'

# @app.get("/read_cookie")
# async def get_cookie(my_cookie: Annotated[str | None, Cookie()] = None):
    
#     print(f'Cookie: {my_cookie}')
#     return my_cookie

@app.post("/auth")
async def authenticate(body:User_Credntial, res:Response):
    if credentials.get(body.username) == body.password:
        res.set_cookie('loggedUser',body.username)
        return 'Authenticated OK'
    else:
        res.status_code = 404
        return 'Error to authenticate'


@app.get("/read_cookie")
async def get_cookie(my_var: Request):
    
    print(f'Cookie: {my_var._cookies}')
    return my_var._cookies

