from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/admin")
def admin():
    return "<h1>Hello, Admin!</h1>"

if __name__ == "__main__":
    app.run(debug=True)