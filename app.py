from flask import Flask, render_template, request, url_for, redirect, session
import rep

app = Flask(__name__)
@app.route("/")
def inicial():
    produtos = rep.produto(1, "racao")
    return render_template ('index.html', produtos=produtos)

@app.route("/produtos/<classe>/<animal>", methods = ["GET"])
def produtos(classe, animal):
    produtos = rep.produto(animal, classe)
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
        nomeCliente = cliente[0][1]
        session['user'] = nomeCliente
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
        rep.realizar_cadastro(nome, email, cpf, celular, endereco, senha, pet, nome_pet)
        return render_template("login.html")
    else:
        return render_template("cadastro.html")

@app.route("/promocao")
def promocao():
    return render_template ('promocao.html')

@app.route("/agendamento", methods = ["GET", "POST"])
def agendamento():
    if request.method == "POST":
        id_pet = request.form["pet"]
        id_profissional = request.form["profissional"]
        data = request.form["data"]
        horario = request.form["horario"]
        rep.agendamento(data=data,horario=horario,id_profissional=id_profissional,id_cliente=4,id_servico=2)
        return render_template ('agendamento.html')
    else:
        return render_template ('agendamento.html')


@app.route("/compra")
def compra():
    return render_template ('compra.html')

app.run(debug=True)


