import pymysql

conn = pymysql.connect("localhost", "root", "rat", "clgdb")

cur = conn.cursor()

#name = input("Enter a name that you want to delete from the databse ")
while True:
    try:
        id = int(input("Enter emp id to update name: "))
        name = input("Enter new name: ")
        break
    except ValueError as V:
        print(V)
    print("Wrong input, try again")


#str = "delete  from emp where NAME ='%s'"%(name)

str = "update emp set name = '%s' where id ='%d'"%(name,id)


data = cur.execute(str)

conn.commit()

print(data, "Record is updated")
#print(data, " record is deleted")

conn.close()



