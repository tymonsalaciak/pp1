class User:
    pass

user1 = User()

user1.fname = "Antoni"
user1.sname = "Kulesza"

print(user1.fname)


class Complex:

    def __init__(self, realpart, imagpart):

        self.r = realpart

        self.i = imagpart


x = Complex(3.0, -4.5)

x.r, x.i