string = "You never get a second chance to make a first impression"
count = 0

def calculatin(string):
    count = 0
    for i in string:
        if i == 'e':
            sum = i + count
            count = 1 + count
    print(sum)

        


calculatin(string)