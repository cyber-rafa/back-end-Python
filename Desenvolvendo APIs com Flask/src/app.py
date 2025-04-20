from flask import Flask , request

app = Flask(__name__)

@app.route('/olamundo/<usuario>/<int:idade>')
def hello_word(usuario, idade):
    print(idade)
    print(f'tipo de variavel idade: {type(idade)}')
    print(f'usuario: { type(usuario)}')
    return f'<h1>Ola mundo! usuario: {usuario}</h1>'

@app.route("/about", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        return "<h1> metodo POST</h1>"
    else:
        return "<h1> metodo GET</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)