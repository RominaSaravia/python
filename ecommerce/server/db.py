from sqlmodel import Field, Session, SQLModel, create_engine, select,delete


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: float | None = Field(default=None, index=True)
    img_url: str = ''

class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    password:str

class Carts(SQLModel, table=True):
    id: int =  Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="users.id")
    product_id: int = Field(default=None, foreign_key="product.id")
    amount: int  # se envía en cada request de POST /cart


sqlite_file_name = "database.db"
sqlite_url = f"postgresql://admin:Xu1oq7zpOpLVcP4oXvneCguhETN5xvhC@dpg-crd24ud2ng1s73fn7j8g-a.oregon-postgres.render.com/aerolinea"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True)


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


def getCart(userId:int):
    with Session(engine) as session:
        cart = session.exec(  select(Carts,Product).where(Carts.product_id == Product.id).where(Carts.user_id == userId)  )
        print('****************************')
        cartProducts = []
        for c, p in cart:
            auxProduct = dict(p)
            auxProduct['amount'] = c.amount
            cartProducts.append(auxProduct)
            print(' auxProduct ---> ', auxProduct)
        return cartProducts

    

def upsertCartProduct(userId, productId, amount):
    with Session(engine) as session:
        cartProduct = session.exec( select(Carts)
                                .where(Carts.user_id == userId)         # WHERE cart.user_id = userId
                                .where(Carts.product_id == productId)   # AND cart.product_id = productId 
                                ).first()
    
        if(cartProduct == None): # si el producto no se encuentra en el carrito...
            cartProduct = Carts(user_id=userId,product_id=productId,amount=amount) # creo nuevo registro del carrito
        else:   # si ya se encuentra en el carrito...
            cartProduct.amount = amount   # sobrescribo el valor de cantidad (amount)

        session.add(cartProduct)
        session.commit()
        session.refresh(cartProduct)
        return cartProduct
    

def deleteCartProduct(userId, productId):
    with Session(engine) as session:
        result = session.exec( delete(Carts)
                                .where(Carts.user_id == userId)         # WHERE cart.user_id = userId
                                .where(Carts.product_id == productId)   # AND cart.product_id = productId 
                                )
        session.commit()
        return result


def authUser(attempEmail,attempPassword):
    with Session(engine) as session:
        user = session.exec( select(Users.id).where(Users.email == attempEmail).where(Users.password == attempPassword) ).first()

    if user != None:
        return user
    
    return None

    
        

