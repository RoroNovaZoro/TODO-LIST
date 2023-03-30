from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
db=SQLAlchemy(app)

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list= db.Column(db.String(500),nullable=False)

    def __repr__(self):
        return f"List('{self.list}')"

@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
        item=request.form.get("suryam")
        listitem=List(list=item)
        db.session.add(listitem)
        db.session.commit()
    k=List.query.all()
    return render_template("index.html",k=k)
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    q=List.query.filter_by(id=todo_id).first()
    db.session.delete(q)
    db.session.commit()
    return redirect(url_for("home"))    

if __name__=="__main__":
    app.run(port=3000,debug=True)    
