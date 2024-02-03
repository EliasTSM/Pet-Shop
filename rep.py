import sqlite3


def cadastro(nome,email,cpf,celular,endereco,senha,pet,nome_pet):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'INSERT INTO humano (nome_humano,cpf_humano,email_humano,contato_humano,endereco_humano,senha) VALUES ("nome","cpf","email","celular","endereco","senha")'
        cursor.execute(sql_select)
        sql_select_pet = f'INSERT INTO clientes (nome_cliente, id_animal) VALUES ("nome_pet","pet")'
        cursor.execute(sql_select_pet)
        conn.commit()
        conn.close()
        msg = ("Dados gravados com sucesso")
    except:
        msg = ("Erro ao inserir os dados")

def produto(tipo_produto,id_animal:int):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM produto WHERE tipo_produto = "{tipo_produto}" AND id_animal = {id_animal}'
        cursor.execute(sql_select)
        racao = cursor.fetchall()      
        conn.close()
        return racao
    except:
        return False
    
def profissional(id_animal:int):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM profissional WHERE id_animal = {id_animal}'
        cursor.execute(sql_select)
        profissional = cursor.fetchall()
        print(profissional)
        conn.close
        return profissional
    except:
        return False
    
produtos = produto("racao", 1)
print(produtos)

    


    

    
        