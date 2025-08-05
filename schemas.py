from pydantic import BaseModel

class LoginRequest(BaseModel):
    login: str
    senha: str

class MenuItem(BaseModel):
    tela: str
    sistema: str
