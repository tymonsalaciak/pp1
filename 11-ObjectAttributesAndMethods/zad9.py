class Array():

    @staticmethod
    def idencticalarray(n,m):
        arr = []
        for i in range(n):
            arr.append(m)
        return arr

    
    @staticmethod
    def random(n,vf,vt):
        import random
        arr = []
        for i in range(n):
            arr.append(random.randint(vf,vt))
        return arr
        


    #@staticmethod
    #def print_in_col(array, vf, vt):
        #arr = []
        #for i in range(array):



print(Array.idencticalarray(10,4))
print(Array.random(20,-7,8))