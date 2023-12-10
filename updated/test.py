import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='root123',database='coursify')
if con.is_connected():
    cursor=con.cursor()
    cursor.execute("insert into `basic_info` (`name`,`city`,`country`,`about`,`profile_url`) values (%s,%s,%s,%s,%s)",('IDK','paris','France',"idk anything",'www.wth.com',))
    con.commit()
    cursor.close()
else:
    print("not connected")