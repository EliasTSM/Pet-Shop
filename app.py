from flask import Flask, render_template, request, url_for
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
    return render_template ('index.html')

@app.route("/produtos/<animal>/<classe>", methods = ["GET"])
def produtos(animal,classe):
    produto = rep.produto(classe,animal)

    return render_template('index.html')

@app.route("/servicos")
def servicos():
    return render_template ('servicos.html')

@app.route("/login")
def login():
    return render_template ('login.html')

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
        
        mensagem = rep.realizar_cadastro(nome, email, cpf, celular, endereco, senha, pet, nome_pet)
        return render_template("resultado_cadastro.html", mensagem=mensagem)
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


