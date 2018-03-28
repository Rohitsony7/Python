import sqlite3

from employee import Employee

conn = sqlite3.connect(':memory:') #Helps you to create virtual database every times you excute

c = conn.cursor()

c.execute("""create TABLE  EMPLOYEE ( first text, second text, pay int)""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT  into EMPLOYEE values(:first, :second, :pay)", {'first':emp.first, 'second':emp.second, 'pay':emp.pay})

def get_emp_by_name(second):
    with conn:
        c.execute("select * from EMPLOYEE where second = :second",{'second':second})
        return c.fetchall()

def remove_emp(emp):
    with conn:
        c.execute("DELETE from EMPLOYEE where first = :first AND second = :second", {'first':emp.first, 'second':emp.second})
        #print(c.fetchall())


emp_1 = Employee('RONNIE', 'SONY', 900000)
emp_2 = Employee('ROHIT', 'SONY',  777777)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp_by_name('SONY')
print(emps)

remove_emp(emp_1)
print(remove_emp(emp_1))

emps = get_emp_by_name('SONY')
print(emps)

conn.close()