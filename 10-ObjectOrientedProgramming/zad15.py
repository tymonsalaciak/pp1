import random
import numpy as np

class thermometer():
    def __init__(self):
        self.tis_on = False


    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False
        


    def temp_meas(self): 
        x = round(random.uniform(34.0, 42.0),1)
        if x > 37.0:
            print(f"temperature {x}C (fever)")
        if x > 41.0:
            print(f"temperature {x}C (fever) CRITICAL TEMPERATURE")
        if x < 37.0:
            print(f"temperature {x}C everything in shape")





t = thermometer()











"""
 Place the class definition 
and the main program in separate files. Then use the program and:
a.	Create a thermometer
b.	Turn thermometer on
c.	Measure temperature
d.	Display temperature
e.	Turn thermometer off
#for i in np.arange(34,42, 0.1):
    #print(i)

x = random.uniform(34.0, 42.0)
for i in np.arange(34.0,42.0, 0.1):
    print(i)


"""
