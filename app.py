from flask import Flask,render_template,url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
                    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(200), nullable=False)
    Description = db.Column(db.String(500), nullable=False)
    Date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Title}"

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['Title']
        desc = request.form['Description']
        todo = Todo(Title=title,Description=desc)
        db.session.add(todo)
        db.session.commit()
        allTodo = Todo.query.all()
        print(allTodo)
    return render_template('index.html',allTodo=Todo.query.all())

@app.route('/show')
def prods():
    allTodo= Todo.query.all()
    print(allTodo)
    return 'these are the products!'

@app.route('/update')
def update():
    allTodo= Todo.query.all()
    print(allTodo)
    return 'these are the products!'

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True,port=8000)