from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    nome = request.args.get("nome", "visitante")
    return f"<p>Hello, {escape(nome)}!</p>"