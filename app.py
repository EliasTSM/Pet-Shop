from flask import Flask, render_template, request, url_for

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

@app.route("/servicos")
def servicos():
    return render_template ('servicos.html')

@app.route("/login")
def login():
    return render_template ('login.html')

@app.route("/cadastro")
def cadastro():
    return render_template ('cadastro.html')

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


