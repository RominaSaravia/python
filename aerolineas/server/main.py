from fastapi import FastAPI
from validations import Ticket,Passenger,Flight,Code_Country
from controller import filterById

app = FastAPI()


ListTickets = [
    Ticket(
        id = 1,
        p = Passenger( id_document=48651567,name="Martha",surname="Smith",email="martha.smith@gmail.com",birth_date="12/01/2024"),
        f = Flight( destination = "ARG",origin="BRA",takeoff_date="12/01/2024")
    )
]


@app.get("/")
async def root():
    return {"message": "Servidor Aeorolineas!"}


@app.post("/ticket")
async def root(ticket:Ticket):
    ListTickets.append(ticket)
    return {'message: Se creo producto'}


@app.get("/ticket")
async def root():
    return ListTickets

@app.get("/ticket/{id}")
async def root(id:int):
    return filterById(id,ListTickets)


