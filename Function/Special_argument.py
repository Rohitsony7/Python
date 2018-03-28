def Student_info(*args, **kwargs):
    print(args)

    print(kwargs)
Student_info("Ronny", "Annie", you = "Medico", me = "Engineer")

A = [1,2,3,4,5,7]
B = {'a':"anu", 'b':"Sonu"}
Student_info(*A,**B) #  for unpack those values






