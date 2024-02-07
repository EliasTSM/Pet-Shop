from flask import Flask, render_template, request, url_for, redirect, session, flash
from app import app
from flask_login import login_user, logout_user, current_user
from user import User
import rep


@app.route("/")
def inicial():
    produtos = rep.produtos(1, "racao")
    return render_template ('index.html', produtos=produtos)

@app.route("/produtos/<classe>/<animal>", methods = ["GET"])
def produtos(classe, animal):
    produtos = rep.produtos(animal, classe)
    return render_template('index.html', produtos=produtos)

@app.route("/servicos")
def servicos():
    return render_template ('servicos.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        cliente = rep.login(email,senha)
        id = cliente[0][0]
        nome = cliente[0][1]
        cpf = cliente[0][1]
        e_mail = cliente[0][1]
        contato = cliente[0][1]
        endereco = cliente[0][1]
        user_dados = User(id, nome, cpf, e_mail, contato, endereco)
        if len(cliente) != 0:
            produtos = rep.produtos(1, "racao")
            login_user(user_dados)
            return render_template("index.html", produtos=produtos)
        else:
            return render_template("login.html")
    
    return render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    produtos = rep.produtos(1, "racao")
    return render_template ('index.html', produtos=produtos)
    

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
        rep.realizar_cadastro(nome, email, cpf, celular, endereco, senha, pet, nome_pet)
        return render_template("login.html")
    else:
        return render_template("cadastro.html")

@app.route("/promocao")
def promocao():
    return render_template ('promocao.html')

@app.route("/agendamento/<servico>", methods = ["GET", "POST"])
def agendamento(servico):
    if (current_user.is_authenticated):
        if request.method == "POST":
            id_pet = request.form["pet"]
            id_profissional = request.form["profissional"]
            data = request.form["data"]
            horario = request.form["horario"]
            rep.agendamento(data=data,horario=horario,id_profissional=id_profissional,id_cliente=4,id_servico=2)
            return render_template ('agendamento.html')
        else:
            return render_template ('agendamento.html')
    else:
        return render_template ('login.html')


@app.route("/compra/<idProduto>")
def compra(idProduto):
    produto = rep.produto(idProduto)
    animal = produto[0][5]
    classe = produto[0][6]
    produtos = rep.produtos(animal, classe)
    return render_template ('compra.html', produto=produto, produtos=produtos)

app.run(debug=True)