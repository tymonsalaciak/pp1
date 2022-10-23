#P = (x,y)

x = int(input("give x: "))
y = int(input("give y: "))


if x >= 0 and y >= 0 :
    print(f'point P({x},{y})is located in first quadrant')
elif x >= 0 and y <= 0 :
    print(f'point P({x},{y})is located in fourth quadrant')
elif x <= 0 and y <= 0 :
    print(f'point P({x},{y})is located in third quadrant')
elif x <= 0 and y >= 0 :
    print(f'point P({x},{y})is located in second quadrant')
else:
    print(f'point is in the position (0,0) ')
