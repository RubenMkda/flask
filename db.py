import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://postgres:uszkXzOd4KoFqQ3tYBkg@containers-us-west-183.railway.app:6858/railway'

def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    s = Session()

    if s != None:
        print("Conexion a base de datos")
    else:
        print("No conectado")

    return s
