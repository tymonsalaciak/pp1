"""
Each book has a title, author, number of pages and the current page number that is currently being read. 
It is possible to open a book - 
then we can read it. If a book is open, it is possible to go to the next or previous page

"""




class Ebook():
    def __init__(self):
        self.title = "boook"
        self.open = False
        self.page = 1
        self.author = "B.G"
        #x = int(input("how mannny pages? "))
        self.num_of_pages = 355


    def open_eb(self):
        self.is_on = True
        

    def page_num(self,num):
        self.page = num

    
    def move_pages(self,strony):
        self.page = self.page + strony


    def read_it(self):
        #if self.open == True:
            count = 1
            x = input("next(+), previous(-)")
            if x == "+":
                count += 1

            if x == "-":
                count -= 1


            c = count

    def book_status(self):
        #if self.open == True:
            print(f"{self.title}, {self.author}, page {}  out of {self.num_of_pages}")



    def close_eb(self):
        self.open = False
        print("you closed the book")





b = Ebook()


b.open_eb()
b.book_status()
b.read_it()
b.read_it()
b.read_it()
b.read_it()

b.book_status()
#b.close_eb()  

b.read_it()


