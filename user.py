from flask_login import UserMixin
from app import lm
import rep

@lm.user_loader
def load_user(id):
    cliente = rep.verificacao(id)
    user = User(cliente[0][0], cliente[0][1], cliente[0][2], cliente[0][3], cliente[0][4], cliente[0][5], cliente[0][6])
    return user

class User(UserMixin):
    def __init__ (self, id, nome, cpf, email, contato, endereco, senha=None):
        self.id = id
        self.nome_humano = nome
        self.cpf_humano = cpf
        self.email_humano = email
        self.contato_humano = contato
        self.endereco_humano = endereco
        self.senha = senha

