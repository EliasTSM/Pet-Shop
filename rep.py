import sqlite3


def realizar_cadastro(nome, email, cpf, celular, endereco, senha, pet, nome_pet):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()

        sql_insert_humano = f'INSERT INTO humano (nome_humano, cpf_humano, email_humano, contato_humano, endereco_humano, senha) VALUES ("{nome}", "{cpf}", "{email}", "{celular}", "{endereco}", "{senha}")'
        cursor.execute(sql_insert_humano)
        
        match pet:
            case "Cachorro":
                id_pet = 1
            case "Gato":
                id_pet = 2
            case "Pássaro":
                id_pet = 4
            case "Hamster":
                id_pet = 3
            case "Porco da India":
                id_pet = 5
            case "Peixe":
                id_pet = 6
        
        sql_insert_cliente = f'INSERT INTO clientes (nome_cliente, id_animal) VALUES ("{nome_pet}", {id_pet})'
        cursor.execute(sql_insert_cliente)
        
        conn.commit()
        conn.close()
        msg = "Dados gravados com sucesso"
    except:
        msg = "Erro ao inserir os dados"

    return msg

def produto(tipo_produto,id_animal:int):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM produto WHERE tipo_produto = "{tipo_produto}" AND id_animal = {id_animal}'
        cursor.execute(sql_select)
        produto = cursor.fetchall()      
        conn.close()
        return produto
    except:
        return False
    
def profissional(id_animal:int):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM profissional WHERE id_animal = {id_animal}'
        cursor.execute(sql_select)
        profissional = cursor.fetchall()
        conn.close
        return profissional
    except:
        return False


    
    


    

    
        