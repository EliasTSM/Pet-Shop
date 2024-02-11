import sqlite3


def gerar_id_humano():
    conn = sqlite3.connect("petshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='humano'")
    id = cursor.fetchone()[0]
    conn.close()
    return id + 1

def realizar_cadastro(nome, email, cpf, celular, endereco, senha, pet, nome_pet):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()

        sql_insert_humano = f'INSERT INTO humano (nome_humano, cpf_humano, email_humano, contato_humano, endereco_humano, senha) VALUES ("{nome}", "{cpf}", "{email}", "{celular}", "{endereco}", "{senha}")'
        cursor.execute(sql_insert_humano)
       
        id_humano = gerar_id_humano()
        sql_insert_cliente = f'INSERT INTO clientes (nome_cliente, id_animal, id_humano) VALUES ("{nome_pet}", {pet}, {id_humano})'
        cursor.execute(sql_insert_cliente)
        
        conn.commit()
        conn.close()
        msg = "Dados gravados com sucesso"
    except:
        msg = "Erro ao inserir os dados"

    return msg

def produtos(id_animal:int, tipo_produto):
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
    
def produto(id_produto:int):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM produto WHERE id_produto = {id_produto}'
        cursor.execute(sql_select)
        produto = cursor.fetchall()      
        conn.close()
        return produto
    except:
        return False

def listaProdutos():
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM produto'
        cursor.execute(sql_select)
        ListaDeProdutos = cursor.fetchall()      
        conn.close()
        return ListaDeProdutos
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
    
def profissional_consulta(id_profissional:int):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM profissional WHERE id_profissional = {id_profissional}'
        cursor.execute(sql_select)
        profissional = cursor.fetchall()
        conn.close
        return profissional
    except:
        return False
    
def login(email,senha:int):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM humano WHERE email_humano = "{email}" AND senha = "{senha}"'
        cursor.execute(sql_select)
        cliente = cursor.fetchall()
        conn.close()
        return cliente
    except:
        False

def verificacao(id):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM humano WHERE id_humano = "{id}"'
        cursor.execute(sql_select)
        cliente = cursor.fetchall()
        conn.close()
        return cliente
    except:
        False


def agendamento(data,horario,id_profissional,id_cliente,id_servico):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'INSERT INTO agendamento (data_agendamento,hora_agendamento,id_profissional,id_cliente,id_servico) VALUES ("{data}","{horario}",{id_profissional},{id_cliente},{id_servico})'
        cursor.execute(sql_select)
        conn.commit()
        conn.close()
        msg = "Dados gravados com sucesso"
        print(data)
        print(horario)
        print(id_profissional)
        print(id_cliente)
        print(id_servico)
        print(msg)
        return msg
    except:
        msg = "Erro ao inserir os dados"
        print(data)
        print(horario)
        print(id_profissional)
        print(id_cliente)
        print(id_servico)
        print(msg)
        return msg

def tipoServico(tipo_servico, id_animal):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT id_servico FROM servicos WHERE id_animal = "{id_animal}" AND tipo_servico = "{tipo_servico}"'
        cursor.execute(sql_select)
        id_servico = cursor.fetchall()
        conn.close()
        return id_servico
    except:
        False


def info_clientes(id_humano):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM clientes WHERE id_humano = "{id_humano}"'
        cursor.execute(sql_select)
        clientes = cursor.fetchall()
        conn.close()
        return clientes
    except:
        False

def info_consulta(id_cliente):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM agendamento WHERE id_cliente = "{id_cliente}"'
        cursor.execute(sql_select)
        consulta = cursor.fetchall()
        conn.close()
        return consulta
    except:
        False

def tipoPet(id_pet):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT id_animal FROM clientes WHERE id_cliente = "{id_pet}"'
        cursor.execute(sql_select)
        idAnimal = cursor.fetchall()
        conn.close()
        return idAnimal
    except:
        False

def servico(id_servico):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM servicos WHERE id_servico = "{id_servico}"'
        cursor.execute(sql_select)
        servico = cursor.fetchall()
        conn.close()
        return servico
    except:
        False

def excluir_consulta(id_consulta):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'DELETE from agendamento WHERE id_agendamento = "{id_consulta}"'
        cursor.execute(sql_select)
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

def excluir_pet(id_pet):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select1 = f'DELETE from agendamento WHERE id_cliente = "{id_pet}"'
        cursor.execute(sql_select1)
        sql_select2 = f'DELETE from clientes WHERE id_cliente = "{id_pet}"'
        cursor.execute(sql_select2)
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

def excluir_conta(id_humano):
    try: 
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        pets = info_clientes(id_humano)
        for pet in pets:
            sql_select1 = f'DELETE from agendamento WHERE id_cliente = "{pet[0]}"'
            cursor.execute(sql_select1)
            sql_select2 = f'DELETE from clientes WHERE id_cliente = "{pet[0]}"'
            cursor.execute(sql_select2)
        sql_select3 = f'DELETE from humano WHERE id_humano = "{id_humano}"'
        cursor.execute(sql_select3)
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

def alterar_dados(nome, email, contato, endereco, senha, id):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_update = "UPDATE humano SET nome_humano = ?, email_humano = ?, contato_humano = ?, endereco_humano = ?, senha = ?  WHERE id_humano = ?"
        cursor.execute(sql_update, (nome, email, contato, endereco, senha, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

def adicionar_pet(nome_cliente, id_animal, id_humano):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_insert_cliente = f'INSERT INTO clientes (nome_cliente, id_animal, id_humano) VALUES ("{nome_cliente}", {id_animal}, {id_humano})'
        cursor.execute(sql_insert_cliente)
        conn.commit()
        conn.close()
        msg = "Dados gravados com sucesso"
    except:
        msg = "Erro ao inserir os dados"
    return msg

        


    
    


    

    
        