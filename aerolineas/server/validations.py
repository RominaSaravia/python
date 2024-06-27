from pydantic import BaseModel
from enum import Enum

class Code_Country(str,Enum):
    ar="ARG"
    br="BRA"
    ur="URU"
    ch="CHI"

class Passenger(BaseModel):
    id_document: int
    name: str
    surname: str
    email: str 
    birth_date: str

class Flight(BaseModel):
    destination:Code_Country
    origin: Code_Country
    takeoff_date:str

class Ticket(BaseModel):
    id:int | None = None
    p:Passenger
    f:Flight




