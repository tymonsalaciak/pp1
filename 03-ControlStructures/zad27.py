for i in range(1,10):
    if i <= 3:
        print(f"{i}", end="\n")
    elif i <= 6:
        print(f"{i}" , end=' ')
    elif i <= 9:
        print(f"{i}" , end='\n')

print("---------")

for i in range(1,10):
    if i <= 3:
        print(f'{i} {i} {i}')
    elif i <= 6:
        print(f'{i} {i} {i}')
    elif i <= 9:
        print(f'{i} {i} {i}')