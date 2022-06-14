from flask import Flask, render_template, request
from sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    complete = db.Column(db.Boolean)

db.create_all()

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/add", methods="POST")
def add_todo():
    if request.method == "POST":
        new_title = request.form["todo"]

if __name__ == '__main__':
    app.run(debug=True)