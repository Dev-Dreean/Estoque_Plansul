from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, CHAR
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    NUSEQUSUARIO = Column(Integer, primary_key=True, index=True)
    CDMATRFUNCIONARIO = Column(CHAR(8), unique=True)
    NMLOGIN = Column(String(30))
    LGATIVO = Column(CHAR(1))
    NOMEUSER = Column(String(80))
    SENHA = Column(String(255))  # hash
    DATOPERACAO = Column(Date)
    HOROPERACAO = Column(Time)
    REGIAO = Column(CHAR(2))
    PERFIL = Column(CHAR(3))
    VERSIST = Column(String(20))

class AcessoTela(Base):
    __tablename__ = "acessotela"
    NUSEQTELA = Column(Integer, primary_key=True, index=True)
    DETELA = Column(String(100))
    NMSISTEMA = Column(String(60))
    FLACESSO = Column(CHAR(1))

class AcessoUsuario(Base):
    __tablename__ = "acessousuario"
    NUSEQTELA = Column(Integer, ForeignKey("acessotela.NUSEQTELA"), primary_key=True)
    CDMATRFUNCIONARIO = Column(CHAR(8), ForeignKey("usuario.CDMATRFUNCIONARIO"), primary_key=True)
    INACESSO = Column(CHAR(1))

