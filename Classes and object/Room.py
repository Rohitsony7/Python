class Room:
    pass
r = Room()
r1 = Room()

print(r)
print(r1)

r.length=10
r.breadth=20
r.height=30

print("AREA r",(r.breadth*r.height*r.length))

r1.length=101
r1.breadth=202
r1.height=302

print("AREA r1",(r1.breadth*r1.height*r1.length))

