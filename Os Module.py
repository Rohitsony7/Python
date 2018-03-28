import os

print(dir(os.walk))

print()

print(os.getcwd())

print(os.listdir(os.getcwd()))

#os.mkdir('DEMO') # to make new directory

#os.rename("RM_DEMO","DEMO")


print()
print(os.stat('Function'))


for dirpath, dirname, filename in os.walk("C:/Users/Rohit/Desktop"):
    print("current_path", dirpath)
    print("Directories", dirname)
    print("Files", filename)
    print()



os.environ.get("HOME")
