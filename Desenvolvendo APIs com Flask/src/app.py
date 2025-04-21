from flask import Flask , request

app = Flask(__name__)

@app.route('/olamundo/<usuario>/<int:idade>/<float:altura>')
def ola_mundo(usuario, idade, altura):
    return{
        "usuario": usuario,
        "idade": idade,
        "altura": altura,
     }

@app.route("/about", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        return "<h1> metodo POST</h1>"
    else:
        return "<h1> metodo GET</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)