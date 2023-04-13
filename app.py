from flask import Flask, make_response, request, render_template, redirect, send_from_directory, session
import db

app = Flask(__name__)

@app.route("/signin", methods=['POST','GET'])
def login():
    return render_template("tela-de-login.html")

@app.route("/signup", methods=["POST", 'GET'])
def signup():
    if request.method == 'POST':
        nome = request.form.get("nome")
        data_nascimento = request.form.get("data_nascimento")
        email = request.form.get("email")
        senha = request.form.get("senha")
        genero = request.form.get("genero")
        print(f'nome: {nome}\ndata nasc: {data_nascimento}\nemail: {email}\nsenha: {senha}\ngenero: {genero}')
        #db.criarUser(name=nome, birthday=data_nascimento,email=email,password=senha,gender=genero)
    return render_template("formulario.html")




if __name__ == "__main__":
    app.run(debug=True)