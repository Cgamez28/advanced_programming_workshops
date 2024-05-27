import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Se borro una segunda instancia que habia en el archivo
app = FastAPI()


"""
como en la consola del navegador estaba dando problemas con el CORS, se configura el cors para que la o las URL
que estan en origins y permita las solicitudes fetch 
"""
origins = [
    "http://127.0.0.1:5500"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

# se configuro de manera correcta de la base de datos PostgreSQL
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True, index=True),
                 Column('name', String, index=True),
                 Column('description', String, index=True))

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ProductCreate(BaseModel):
    name: str
    description: str

@app.get("/get_products")
def get_products(db: Session = Depends(get_db)):
    query = select(products)
    result = db.execute(query).fetchall()
    return [{"id": row.id, "name": row.name, "description": row.description} for row in result]

@app.post("/create_products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = products.insert().values(name=product.name, description=product.description)
    db.execute(new_product)
    db.commit()
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
