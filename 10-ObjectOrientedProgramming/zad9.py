#operatory z self pod init

class TV():
    def __init__(self):
        self.is_on = False 
        self.chanel_no = 1
        self.chanels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
        self.kanaly = {"TVP1": 1, "TVP2": 2, "Polsat": 3, "TVN": 4, "Filmbox": 5, "Discovery": 6}

    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False

    

    def set_channel(self, num):
        self.chanel_no = num  


    def set_channels(self): 
        add_chanel = input("dodaj kanał: ")
        self.chanels.append(add_chanel)

    
    def show_channels(self):   
        print(self.chanels)


    def show_status(self):
        if self.is_on == True:
            print("you can increase volume 0-10 by using +  or -")
            addd = input("increase or decrease vol: ")
            vol = 0
            if addd == "+":
                add = int(input("vol: "))
                vol =+ add

            if addd == "-":
                dec = int(input("vol: "))
                vol =- dec
                
            for key in self.kanaly:
                x = self.kanaly[key]
                #print(key, self.kanaly[key] )



            print(f"tv is on, chanel {self.chanel_no}, {key},vol lvl {vol}")
            #print(self.chanels)
    
        else:
            print("tv is off")




p1 =TV()

p1.show_status()
p1.turn_on()
p1.set_channel(4)


p1.show_status()

p1.turn_off()
p1.show_status()
p1.turn_on()
p1.show_status()
p1.show_status()
p1.show_status()


#i = int(input("add chanel: "))
        #self.chanel_no = self.chanels.append(i)
  