import sqlite3
from employee import Employee





conn = sqlite3.connect('Employee.db')

c = conn.cursor()

#c.execute("""CREATE TABLE Employee     (
#                                          first text,
#                                           second text,
#                                           pay integer
#                                            )""")
emp1 = Employee("Anushree", "soni", 90000)
emp2 = Employee("Tina", "soni", 90000)


c.execute("INSERT into Employee values (?, ?, ?)",(emp1.first, emp1.second, emp1.pay)) # for tuple
conn.commit()

c.execute("INSERT into Employee values(:first, :second , :pay )",{'first':emp2.first, 'second':emp2.second, 'pay':emp2.pay}) # for dictionary and key values
conn.commit()

#c.execute("INSERT into Employee VALUES ('ROHIT', 'Soni', 90000)")

#c.execute("INSERT into Employee VALUES ('RONNY', 'Soni', 70000)")

c.execute("SELECT * from Employee where second = 'soni' ")
print(c.fetchmany(2))

print(c.rowcount)


num = 0
while True:
    num += 1
    result = c.fetchone()
    print(result[0],":", result[1], ":", result[2])

    if num ==2:
        break

conn.commit()
conn.close()