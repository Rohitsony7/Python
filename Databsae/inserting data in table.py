import pymysql

con = pymysql.connect("localhost", "root", "rat", "clgdb")
cur = con.cursor()

#query = " create table emp3(id int(3), name varchar(10)) "

#id = int(input("Enter id"))
#name = input("Enetr name of the person")

#query = "INSERT  into emp() VALUES ('%d', '%s')"%(id,name)
query = "SELECT * FROM EMP "

data = cur.execute(query)
print(data)
result = cur.fetchall()
con.commit()

print("Total record", cur.rowcount)

for num in result:
    id = num[0]
    name = num[1]
    print(id, ":", name)

print(cur.fetchall())

# print(data, "record inserted")

con.close()

