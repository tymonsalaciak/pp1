#operatory z self pod init

class TV():
    def __init__(self):
        self.is_on = False 
        self.chanel_no = 1
        self.chanels = []

    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False

    

    def set_channel(self, num):
        self.chanel_no = num  
        

    def show_status(self):
        if self.is_on == True:
            print(f"tv is on, chanel {self.chanel_no}")
            #print(self.chanels)
    
        else:
            print("tv is off")




p1 =TV()

p1.show_status()
p1.turn_on()
p1.set_channel(5)
p1.show_status()
p1.turn_off()
p1.show_status()
p1.turn_on()
p1.show_status()


#i = int(input("add chanel: "))
        #self.chanel_no = self.chanels.append(i)
  