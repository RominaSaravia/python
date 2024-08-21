from sqlmodel import Field, Session, SQLModel, create_engine, select,delete


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: float | None = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def readAllProducts(search:str=''):
    with Session(engine) as session:
        products = []
        if(search != None or search != '' ):
            products = session.exec(select(Product).where(Product.name.like(f'%{search}%'))).all()
        else:
            products = session.exec(select(Product)).all()
                
        return products

def createNewProduct(prod:Product):
    with Session(engine) as session:
        session.add(prod)
        session.commit()
        session.refresh(prod)
        return prod

def deleteProduct(id:int):
    with Session(engine) as session:
        result = session.exec(delete(Product).where(Product.id == id))
        session.commit()
        return result
