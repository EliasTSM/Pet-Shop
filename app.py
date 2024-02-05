from flask import Flask, render_template, request, url_for, redirect
import rep
# tabela animal: 
# 1 = cachorro
# 2 = gato
# 3 = hamster
# 4 = passaro
# 5 = porquinho
# 6 = peixe

# tabela produtos:
# id_animal
# tipo_produto
# racao, acessorio, medicamento, higienie, brinquedo

app = Flask(__name__)
@app.route("/")
def inicial():
    produtos = rep.produto("racao",1)
    return render_template ('index.html', produtos=produtos)

@app.route("/produtos/<animal>/<classe>", methods = ["GET"])
def produtos(animal,classe):
    
    produto = rep.produto(classe,animal)
    
    for produto in produto:
    
        id_produto, nome_produto, descricao_produto, valor_produto, quantidade_produto, id_animal, tipo_produto, imagem = produto
        print(f"ID: {id_produto}")
        print(f"Nome: {nome_produto}")
        print(f"Descrição: {descricao_produto}")
        print(f"Valor: R$ {valor_produto}")
        print(f"Quantidade: {quantidade_produto}")
        print(f"Tipo: {tipo_produto}")
        print(f"Imagem: {imagem}")

    return render_template('index.html', id_produto=id_produto,nome_produto=nome_produto,descricao_produto=descricao_produto,valor_produto=valor_produto,quantidade_produto=quantidade_produto,tipo_produto=tipo_produto,imagem=imagem)

@app.route("/servicos")
def servicos():
    return render_template ('servicos.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        cliente = rep.login(email,senha) 
        nomeCliente = cliente[0][1]
        if len(cliente) != 0:
            produtos = rep.produto("racao",1)
            return render_template("index.html", user=nomeCliente, produtos=produtos)
        else:
            return render_template("login.html")
    

    return render_template("login.html")
    

@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        cpf = request.form["cpf"]
        celular = request.form["celular"]
        endereco = request.form["endereco"]
        senha = request.form["senha"]
        pet = request.form["pet"]
        nome_pet = request.form["nomePet"]
        print(nome,email,cpf,celular)
        rep.realizar_cadastro(nome, email, cpf, celular, endereco, senha, pet, nome_pet)
        return render_template("login.html")
    else:
        return render_template("cadastro.html")

@app.route("/promocao")
def promocao():
    return render_template ('promocao.html')

@app.route("/agendamento")
def agendamento():
    return render_template ('agendamento.html')

@app.route("/compra")
def compra():
    return render_template ('compra.html')

app.run(debug=True)


