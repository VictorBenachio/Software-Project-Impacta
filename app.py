from flask import *
import db

app = Flask(__name__)

@app.route("/signin")
def login():
    return render_template("tela-de-login.html")

...
@auth.route('/signin', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = db.lerUser(email=email)
    if not user or user.password != password:
        flash('Please check your login details and try again.')
        return render_template("tela-de-login.html")
    return render_template("tela-logado")

@app.route("/signup", methods=["POST", 'GET'])
def signup():
    if request.method == 'POST':
        nome = request.form.get("nome")
        data_nascimento = request.form.get("data_nascimento")
        email = request.form.get("email")
        senha = request.form.get("senha")
        genero = request.form.get("genero")
        print(f'nome: {nome}\ndata nasc: {data_nascimento}\nemail: {email}\nsenha: {senha}\ngenero: {genero}')
        db.criarUser(name=nome, birthday=data_nascimento,email=email,password=senha,gender=genero)
    return render_template("formulario.html")




if __name__ == "__main__":
    app.run(debug=True)