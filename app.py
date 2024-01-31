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


app.run(debug=True)


