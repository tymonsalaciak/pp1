"""
23.	The announcement regarding the temperature forecast in degrees 
Celsius for the next three days was published on the Internet:
"Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
Create a program that calculates the average temperature. 
Use regular expressions to extract the values of temperatures from the message.
average
"""


import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)# odrawu zwraca liste findall?


temp = []
for t in temperatures:
    t = int(t)
    temp.append(t)

sumall = sum(temp) 
print(temp)

average = sumall/len(temp)

print(average,"C")

#print(temperatures)

