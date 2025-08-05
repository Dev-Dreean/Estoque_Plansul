from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario, AcessoUsuario, AcessoTela
from schemas import LoginRequest, MenuItem

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.NMLOGIN == data.login, Usuario.SENHA == data.senha, Usuario.LGATIVO == 'S').first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"matricula": user.CDMATRFUNCIONARIO, "nome": user.NOMEUSER}

@router.get("/menu/{matricula}")
def get_menu(matricula: str, db: Session = Depends(get_db)):
    acesso = (
        db.query(AcessoTela)
        .join(AcessoUsuario, AcessoTela.NUSEQTELA == AcessoUsuario.NUSEQTELA)
        .filter(AcessoUsuario.CDMATRFUNCIONARIO == matricula, AcessoUsuario.INACESSO == 'S')
        .all()
    )
    return [{"tela": a.DETELA, "sistema": a.NMSISTEMA} for a in acesso]

@router.get("/verifica_acesso/{matricula}/{id_tela}")
def verifica_acesso(matricula: str, id_tela: int, db: Session = Depends(get_db)):
    acesso = (
        db.query(AcessoUsuario)
        .filter(
            AcessoUsuario.CDMATRFUNCIONARIO == matricula,
            AcessoUsuario.NUSEQTELA == id_tela,
            AcessoUsuario.INACESSO == 'S'
        )
        .first()
    )
    if not acesso:
        raise HTTPException(status_code=403, detail="No momento você está sem acesso a este item")
    return {"acesso": "liberado"}

@router.get("/todas_telas")
def listar_todas_telas(db: Session = Depends(get_db)):
    telas = db.query(AcessoTela).all()
    return [{"id": t.NUSEQTELA, "tela": t.DETELA, "sistema": t.NMSISTEMA} for t in telas]
