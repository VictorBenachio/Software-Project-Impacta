from flask import Flask, make_response, request, render_template, redirect, send_from_directory, session


app = Flask(__name__)

@app.route("/login")
def homepage():
    return "Teste"

@app.route("/signin", methods=['POST','GET'])
def login():
    return render_template("tela-de-login.html")

@app.route("/signup", methods=["POST"])
def signup():
    if request.method == 'POST':
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        email = request.form.get("email")
        genero = request.form.get("genero")
        print(genero)
        data_nascimento = request.form.get("data_nascimento")
    return render_template("formulario.html")




if __name__ == "__main__":
    app.run(debug=True)