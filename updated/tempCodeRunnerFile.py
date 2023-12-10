import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='root123',database='coursify')
if con.is_connected:
    print("db connected")
else:
    print("db not connected")

cursor=con.cursor()
cursor.execute("select `picture` from `basic_info`;")
col=cursor.fetchall()
cursor.close()

print(col[0][0])
#https://media.licdn.com/dms/image/D4D03AQFDBEzuzf6eYA/profile-displayphoto-shrink_400_400/0/1690283617908?e=1705536000&v=beta&t=-YhiPP7UeBIOsbtBvChmjXABlMAo4MzJKMHVmwLqKko