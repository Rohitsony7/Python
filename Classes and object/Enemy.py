class Enemy:
    life = 3
    def Look(self):
        self.life-=1
        print("Hitted by a Look of your better half")
    def LookLeft(self):
         if self.life<=0:
             print("REST IN PEACE")
         else:
             print(str(self.life) + " Life Left")


baby = Enemy()
baby1 = Enemy()

baby.Look()
baby.Look()
baby.LookLeft()

baby1.LookLeft()


