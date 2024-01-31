import sqlite3


def produto(tipo_produto,id_animal:int):
    try:
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        sql_select = f'SELECT * FROM produto WHERE tipo_produto = "{tipo_produto}" AND id_animal = {id_animal}'
        cursor.execute(sql_select)
        racao_2 = cursor.fetchall()
        print(racao_2)
        conn.close()
        return racao_2
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
    

    


    

    
        