from flask import Flask, render_template, request, url_for

app = Flask(__name__)
@app.route("/")
def inicial():
    return render_template ('index.html')

app.run(debug=True)
