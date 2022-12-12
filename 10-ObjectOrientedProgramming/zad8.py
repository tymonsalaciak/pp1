class TV():
    def __init__(self):
        self.is_on = False 

    def turn_on(self):
        self.is_on = True
        #print("tv is on")

    def turn_off(self):
        self.is_on = False
        #print("tv is off")

    def show_status(self):
        if self.is_on:
            print("tv is on")
            #print(self.is_on)
        else:
            print("tv is off")




p1 =TV()

p1.show_status()
p1.turn_on()
p1.show_status()
p1.turn_off()
p1.show_status()