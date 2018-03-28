import pymysql

conn = pymysql.connect("localhost", "root", "rat", "clgdb")

cur = conn.cursor()

name = (input("Enter name: "))

query = "select * from emp where name = ('%s')"%(name)

data = cur.execute(query)

count = cur.rowcount

print("Total matching record :",count)

conn.commit()

# result = cur.fetchone()

num = 1
while num <= count:
    result = cur.fetchone()

    print(result[0], ":", result[1])
    num += 1

conn.close()