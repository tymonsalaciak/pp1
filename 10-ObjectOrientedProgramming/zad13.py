#the show_status() method. 
# Then check the operation of the TV by adjusting and displaying its volume level.


class TV():
    def __init__(self):
        self.is_on = False 

    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False

    def set_channel(self, num):
        self.chanel_no = num  



    def show_status(self):
        if self.is_on == True:
            print("you can increase volume 0-10")
            add = int(input("increase or decrease vol: "))
            vol = 0
            if add > 0:
                vol =+ add
            else:
                vol =- add
            #print(vol)

            print(f"tv is on, chanel {self.chanel_no}{vol}")
            #print(self.chanels)
    
        else:
            print("tv is off")


  
    



p1 =TV()

p1.show_status()
p1.turn_on()

p1.show_status()

p1.turn_off()
p1.show_status()
p1.turn_on()
p1.show_status()

