import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://fllvnawvuihaxp:79873c989178c12546c2d20b6d224ac5e4229aecb4415fd735e7203310aa61e5@ec2-52-204-157-26.compute-1.amazonaws.com:5432/de8jf9e9fknh92'

#postgres://manolo_user:CEfdCGJDMO5UdmyhPlqkDHy208iqjirc@dpg-cfrrbkcgqg46pjod8oj0-a.oregon-postgres.render.com/manolo

def conectar():
    engine = create_engine(os.environ.get('DATABASE_URL'))
    Session = sessionmaker(bind=engine)
    s = Session()

    if s != None:
        print("Conexion a base de datos")
    else:
        print("No conectado")

    return s