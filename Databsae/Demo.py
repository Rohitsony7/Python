import pymysql

con = pymysql.connect("localhost", "root", "rat", "clgdb")
cur = con.cursor()
cur.execute("select version()")
data = cur.fetchone()
con.close()
print(data)


