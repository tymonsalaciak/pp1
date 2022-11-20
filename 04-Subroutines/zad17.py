string = "You never get a second chance to make a first impression"


def calculatin(string):
    count = 0
    for i in string:
        if i == 'e':
            count = 1 + count
    print(count)

        


calculatin(string)