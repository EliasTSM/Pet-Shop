from flask import Flask, render_template, request, url_for, redirect, session, flash
from app import app
from flask_login import login_user, logout_user, current_user
from user import User
import rep


@app.route("/")
def inicial():
    produtos = rep.produtos(1, "racao")
    listaProdutos = rep.listaProdutos()
    return render_template ('index.html', produtos=produtos, listaProdutos = listaProdutos)

@app.route("/produtos/<classe>/<animal>", methods = ["GET"])
def produtos(classe, animal):
    produtos = rep.produtos(animal, classe)
    listaProdutos = rep.listaProdutos()
    return render_template ('index.html', produtos=produtos, listaProdutos = listaProdutos)

@app.route("/servicos")
def servicos():
    return render_template ('servicos.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        cliente = rep.login(email,senha)
        if len(cliente) != 0:
            id = cliente[0][0]
            nome = cliente[0][1]
            cpf = cliente[0][1]
            e_mail = cliente[0][1]
            contato = cliente[0][1]
            endereco = cliente[0][1]
            user_dados = User(id, nome, cpf, e_mail, contato, endereco)
            produtos = rep.produtos(1, "racao")
            login_user(user_dados)
            listaProdutos = rep.listaProdutos()
            return render_template ('index.html', produtos=produtos, listaProdutos = listaProdutos)
        else:
            flash("Email ou senha inválidos.")
            return render_template("login.html")
    
    return render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    produtos = rep.produtos(1, "racao")
    listaProdutos = rep.listaProdutos()
    return render_template ('index.html', produtos=produtos, listaProdutos = listaProdutos)
    

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
        return redirect(url_for('login'))
    else:
        return render_template("cadastro.html")
    
@app.route("/savePet", methods=["GET", "POST"])
def cadastrar_pet():
    nomePet = request.form.get("nomePetModal")
    pet = request.form.get("petModal")
    rep.adicionar_pet(nomePet, pet, current_user.id)
    flash("Pet cadastrado com sucesso!")
    return redirect(url_for('perfil'))


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
            if (servico == "veterinario"):
                tipo_servico = "Consulta Veterinária"
            else:
                tipo_servico = "Banho e Tosa"

            id_animal = rep.tipoPet(id_pet)
            id_servico = rep.tipoServico(tipo_servico, id_animal[0][0])
            rep.agendamento(data=data,horario=horario,id_profissional=id_profissional,id_cliente=id_pet,id_servico=id_servico[0][0])
            flash("Agendamento realizado com sucesso!")
            return render_template ('agendamento.html', servico = servico)
        else:
            pets = rep.info_clientes(current_user.id)
            return render_template ('agendamento.html', servico = servico, pets = pets)
    else:
        return redirect(url_for('login'))

@app.route("/perfil", methods = ["GET", "POST"])
def perfil():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        celular = request.form["celular"]
        endereco = request.form["endereco"]
        senha = request.form["senha"]
        rep.alterar_dados(nome, email, celular, endereco, senha, current_user.id)
        info = rep.verificacao(current_user.id)
        pets = rep.info_clientes(current_user.id)
        todasConsultas = []
        for pet in pets:
            consultas = rep.info_consulta(pet[0])
            for consulta in consultas:
                profissional = rep.profissional_consulta(consulta[3])
                servico = rep.servico(consulta[5])
                infoConsulta = (consulta[0], pet[1], profissional[0][1], servico[0][1], consulta[1], consulta[2])
                todasConsultas.append(infoConsulta)
        flash("Dados atualizados com sucesso.")
        return redirect(url_for('perfil', pets = pets, consultas = todasConsultas))
    else:
        infos = rep.verificacao(current_user.id)
        pets = rep.info_clientes(current_user.id)
        todasConsultas = []
        for pet in pets:
            consultas = rep.info_consulta(pet[0])
            for consulta in consultas:
                profissional = rep.profissional_consulta(consulta[3])
                servico = rep.servico(consulta[5])
                infoConsulta = (consulta[0], pet[1], profissional[0][1], servico[0][1], consulta[1], consulta[2])
                todasConsultas.append(infoConsulta)
        return render_template ('perfil.html', pets = pets, consultas = todasConsultas)
    
@app.route("/delete/<tabela>/<id>", methods = ["GET", "POST"])
def deletar(tabela, id):
    if tabela == "consulta":
        rep.excluir_consulta(id)
        info = rep.verificacao(current_user.id)
        pets = rep.info_clientes(current_user.id)
        todasConsultas = []
        for pet in pets:
            consultas = rep.info_consulta(pet[0])
            for consulta in consultas:
                profissional = rep.profissional_consulta(consulta[3])
                servico = rep.servico(consulta[5])
                infoConsulta = (consulta[0], pet[1], profissional[0][1], servico[0][1], consulta[1], consulta[2])
                todasConsultas.append(infoConsulta)
        flash("Consulta desmarcada com sucesso.")
        return redirect(url_for('perfil', pets = pets, consultas = todasConsultas))
    elif tabela == "pet":
        rep.excluir_pet(id)
        info = rep.verificacao(current_user.id)
        pets = rep.info_clientes(current_user.id)
        todasConsultas = []
        for pet in pets:
            consultas = rep.info_consulta(pet[0])
            for consulta in consultas:
                profissional = rep.profissional_consulta(consulta[3])
                servico = rep.servico(consulta[5])
                infoConsulta = (consulta[0], pet[1], profissional[0][1], servico[0][1], consulta[1], consulta[2])
                todasConsultas.append(infoConsulta)
        flash("Pet deletado com sucesso.")
        return redirect(url_for('perfil', pets = pets, consultas = todasConsultas))
    else:
        logout_user()
        rep.excluir_conta(id)
        flash("Conta deletado com sucesso.")
        return redirect(url_for('login'))

@app.route("/compra/<idProduto>")
def compra(idProduto):
    produto = rep.produto(idProduto)
    animal = produto[0][5]
    classe = produto[0][6]
    produtos = rep.produtos(animal, classe)
    return render_template ('compra.html', produto=produto, produtos=produtos)

app.run(debug=True)