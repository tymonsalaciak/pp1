class Arrays():

    @staticmethod #dekorator ta metoda poniżej to metoda statyczna - nie ma self 
    def print_in_col(array): # nie trzeba wywołać obiektu
        #for c in array:
            print(*array, sep=", ")
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)

#pole statyczne??
