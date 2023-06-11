from flask import *
import db
from flask_login import login_user, logout_user, LoginManager

app = Flask(__name__)

@app.route("/signin")
def login():
    return render_template("tela-de-login.html")

...
@app.route('/signin', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = db.lerUser(email=email)
    if not user or user.password != password:
        flash('Please check your login details and try again.')
        print("Login Failed")
        return render_template("tela-de-login.html")
    login_user(user)
    print("Login Success")

@app.route("/signup", methods=["POST", 'GET'])
def signup():
    if request.method == 'POST':
        nome = request.form.get("nome")
        data_nascimento = request.form.get("data_nascimento")
        email = request.form.get("email")
        senha = request.form.get("senha")
        genero = request.form.get("genero")
        db.criarUser(name=nome, birthday=data_nascimento,email=email,password=senha,gender=genero)
    return render_template("formulario.html")

@app.route('/habits', methods=['GET'])
def habit_get():
    return render_template("cadastro_habitos.html")

@app.route('/habits', methods=['POST'])
def habit_post():
    name = request.form.get('input--new--habito')

@app.route('/logout', methods=['POST'])
def logout():
    return render_template("tela-de-login.html")


if __name__ == "__main__":
    app.run(debug=True)
