from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.create_all()
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    complete = db.Column(db.Boolean)



@app.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

@app.post("/add")
def add_todo():
    new_title = request.form.get("title")
    new_todo = Todo(title=new_title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)