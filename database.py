from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_USER = "plansul04"
DB_PASS = "SENHA_AQUI"
DB_HOST = "mysql.plansul.kinghost.net"
DB_NAME = "plansul04"
DB_PORT = 3306

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()