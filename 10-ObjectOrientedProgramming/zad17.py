class Statistics():
    def __init__(self):
        self.set = []


    def append(self,num):
        #self.i = num
        x = self.set.append(num)
        return x

    def display(self):
        c = self.set
        #for i in self.set.split():
        print(*c, sep = " ") 

    def max(self):
        c = max(self.set)
        #return c
        print(c)

    def min(self):
        n = min(self.set)
        #eturn n
        print(n)

    def arithmetic(self):
        a = sum(self.set)/len(self.set) 
        #return a
        print(a)


    def median(self):
        if len(self.set) % 2 == 0:
            pass
        else:
            c = len(self.set) // 2
            u = self.set[c]
            #return u
            print(u)


    def showR(self,):
        pass


#joined_string = ' '.join([str(v) for v in L])
#print(joined_string)

d= Statistics()
 
d.append(12)
d.append(37)
d.append(6)
d.append(9)
d.append(17)

d.display()
d.max()
d.min()
d.arithmetic()
d.median()
