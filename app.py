from flask import Flask,render_template,request,redirect
from db import connection_db
app=Flask(__name__)
@app.route('/')
def index():
    con=connection_db()
    cur=con.cursor(dictionary=True)
    cur.execute("select* from students")
    students=cur.fetchall()
    cur.close()
    con.close()
    return render_template("form.html",students=students)
@app.route('/add',methods=['post'])
def add_student():
    name=request.form['name']
    email=request.form['email']
    course=request.form['course']
    con=connection_db()
    cur=con.cursor()
    cur.execute("insert into students(name,email,course) values (%s,%s,%s)",(name,email,course))
    con.commit()
    cur.close()
    con.close()
    return redirect('/')
@app.route('/delete1/<id>')
def delete1(id):
    con=connection_db()
    cur=con.cursor()
    cur.execute("delete from students where id=%s",(id,))
    con.commit()
    cur.close()
    con.close()
    return redirect('/')
@app.route('/edit/<id>',methods=['GET'])
def edit(id):
    con=connection_db()
    cur=con.cursor(dictionary=True)
    cur.execute("select * from students where id=%s",(id,))
    student=cur.fetchone()
    con.commit()
    cur.close()
    con.close()
    return render_template("edit.html",student=student)
@app.route('/update1/<id>',methods=['post'])
def upd(id):
    name=request.form['name']
    email=request.form['email']
    course=request.form['course']
    con=connection_db()
    cur=con.cursor()
    cur.execute("update students set name=%s,email=%s,course=%s where id=%s",(name,email,course,id))
    con.commit()
    cur.close()
    con.close()
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)

