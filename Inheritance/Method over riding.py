class Demo:
    def show(self):
        print("Super class show method called")


class useDemo(Demo):
    def show(self):
        print("Sub class show method called")
        super().show()


obj = useDemo()
obj.show()
