from flask import Flask,render_template,request,url_for,redirect,session
import mysql.connector



con=mysql.connector.connect(host='sql6.freesqldatabase.com',user='sql6637376',password='4Vq7Ug7Lfn',database='sql6637376')
if con.is_connected:
    print("db connected")
else:
    print("db not connected")

app=Flask(__name__,template_folder='template')
app.secret_key='xdjshfksd'

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=="POST":
        uname=request.form['uname']
        upass=request.form['pas']   
        cursor=con.cursor()
        cursor.execute("SELECT `username`,`password`,`name`,`count` FROM `member` WHERE `username`=%s and `password`=%s",(uname,upass))
        record=cursor.fetchall()
        cursor.close()
        if record:
            session['logedin']=True
            session['username']=record[0][2]
            count=[1,2,3]
            return render_template('test.html',username=session['username'],count=count)
        else:
            error='Username or password mismatch'
            return render_template('test.html',error=error)
    else:
        return render_template("test.html")
if __name__=='__main__':
    app.run(debug=True)