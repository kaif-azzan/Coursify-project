from flask import Flask,render_template,request,url_for,redirect,session
import mysql.connector
import csv



con=mysql.connector.connect(host='sql12.freesqldatabase.com',user='sql12645256',password='PI8s6a42uc',database='sql12645256')
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
        cursor.execute("SELECT `username`,`password`,`name` FROM `member` WHERE `username`=%s and `password`=%s",(uname,upass))
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

def letter():
    if request.method=="POST":
        arr=[]
        emaill=request.form['emaill']
        arr.append(emaill)
        return render_template('test.html')




@app.route('/signup',methods=['GET','POST'])
def signup():
        if request.method=="POST":
            uname=request.form['newuname']
            upass=request.form['newpass']
            name=request.form['fname']
            email=request.form['email']
            
            box1=request.form.get('mycheckbox1')
            box2=request.form.get('mycheckbox2')
            
            if box1=='on' and box2==None or box1==None and box2=='on':
                if box1:
                    role='recruiter'
                else:
                    role='job seeker'
                cursor=con.cursor()
                cursor.execute("SELECT `username` FROM `member` WHERE `username`=%s",(uname,))
                record=cursor.fetchall()
                cursor.close()
                if record:
                    error='Username already in use, Pick something new'
                    return render_template("signup.html",error=error)
                else:
                    cursor=con.cursor()
                    cursor.execute("SELECT `email` FROM `member` WHERE `email`=%s",(email,))
                    record=cursor.fetchall()
                    cursor.close()
                    if record:
                        error='email already in use'
                        return render_template("signup.html",error=error)
                    else:
                        cursor=con.cursor()
                        cursor.execute("INSERT INTO `member` (`username`, `password`,`name`,`email`,`role`) VALUES (%s,%s,%s,%s,%s)",(uname,upass,name,email,role))
                        con.commit()
                        cursor.close()
                        return render_template('test.html')
            else:
                    error="Please only select one box"
                    return render_template('signup.html',error=error)
        else:
            return render_template('signup.html')






@app.route('/homepage')
def start():
    count=[1,2,3]
    rows = []
    summ=[]
    imp=[]
    
    
    with open("test.csv", 'r') as file:
        csvreader = csv.reader(file)
        #header = next(csvreader)
        for row in csvreader:
            rows.append(row)

    with open("sum.csv", 'r') as file:
        csvreader = csv.reader(file)
        #header = next(csvreader)
        for row in csvreader:
            summ.append(row)     

    with open('demo.csv','r') as file:
        csvreader=csv.reader(file)
        for row in csvreader:
            imp.append(row)

    with open("demo.csv",'r') as file:
        csvreader=csv.reader(file)
        for i in csvreader:
            temp_value_for_skills=i

    converted_skills_to_list=temp_value_for_skills[0].split()


    col=[]
    with open("sum.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            col.append(row)

    final=[]

    for j in range(0,len(col)):
        converted_summary_to_str=str(col[j])

        counter=0

        for i in range(0,len(converted_skills_to_list)):
            if converted_skills_to_list[i] in converted_summary_to_str:
                counter+=1
        final.append(counter)
    
    
    return render_template('try2.html',count=count,var1=rows[0][0],var2=rows[0][1],var3=rows[0][2],summary=summ[0][0],ish=imp[0],work=rows)








@app.route('/skill',methods=['GET','POST'])
def enter():
    uskills=[]
    ucountry=[]
    ustate=[]
    
    
    if request.method=='POST':
        uskills.append(request.form['skills'])
        ucountry.append(request.form['country'])
        ustate.append(request.form['state'])

        with open('demo.csv','w') as new_file:
            csv_writer=csv.writer(new_file, delimiter=' ')
            csv_writer.writerow(uskills)
        
        
        
        
        return render_template('skill.html')
    else:
        return render_template('skill.html')

if __name__=='__main__':
    app.run(debug=True)