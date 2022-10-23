"""19.	Write a program that calculates a dogs age in 
dogs years. For the first two years, a dog
s life is equal to 10.5 human years. After that 
each dog year is equal to 4 human years. Sample result:
Enter the dog s age in human years: 15
The dog's age in dog’s years is 73 years."""

x = int(input("give dog age: "))
y = x - 2
age1 = x - y

firtyears = age1 * 10.5
secundyears = y * 4
dogAge = firtyears * secundyears

print(f'The dogs age in dogs years is {int(dogAge)} years')