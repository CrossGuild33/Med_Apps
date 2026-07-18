from flask import Flask, request
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db.init_app(app)
@app.route("/")
def hello_world():
    nome = request.args.get("nome", "visitante")
    return f"<p>Hello, {escape(nome)}!</p>"