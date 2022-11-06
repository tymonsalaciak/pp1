def month(n):
    n = n-1
    months = {"January" : 1 , 
    "February":2, 
    "March":3, 
    "April": 4,
    "May" :5, 
    "June": 6, 
    "July": 7,
    "August": 8, 
    "September": 9, 
    "October": 10 ,
    "November": 11  ,
    "December": 12 }
    x = list(months)[n]
    print(x)

month(7)

