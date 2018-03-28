import pymysql

con = pymysql.connect("localhost", "root", "rat", "clgdb")

cur = con.cursor()

cur.execute("select version()")

data = cur.fetchall()

print(data)

con.commit()

con.close()



