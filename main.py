from fastapi import FastAPI
from database import create_table, create_user, login_db, delete_user,show_all
from auth import criptografa

app = FastAPI()

create_table()

@app.post("/register")
def register(email:str , senha:str ):
    senha_S = criptografa(senha)
    return create_user(email, senha_S)

@app.post("/login")
def login_user(email:str , senha:str ):
    senha_S = criptografa(senha)
    return login_db(email, senha_S)

@app.delete("/del")
def deletar_user(email:str , senha:str):
    senha_S = criptografa(senha)
    return delete_user(email, senha_S)

@app.get("/read")
def read_users():
    return show_all()



