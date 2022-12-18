"""
MeatAndFish.txt
GrainsAndBread.txt
Then write a program that creates a shoppinglist.txt file, 
in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.
"""



with open("MeatAndFish.txt", "r", encoding="utf-8") as meatfile:
    e1 = meatfile.read()
    with open("GrainsAndBread.txt", "r", encoding="utf-8") as breadfile:
        e2 = breadfile.read()
        with open("shoppinglistfor18.txt", "a", encoding="utf-8") as shoppinglist:
            shoppinglist.write(e1)
            shoppinglist.write(e2)