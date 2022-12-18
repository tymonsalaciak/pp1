"""
15.	Find any text file on the Internet that contains at least 30 lines of text and download 
that file to your computer. Then write a program that displays the first five lines from the 
file and then waits for the Enter key to be pressed. Then repeat displaying the next five 
lines from the file, waiting for the Enter key to be pressed each time.
"""

with open("filefor15.txt", "r", encoding="utf-8") as f:
    
    i = 0
    for line in f:
        print(line) #drukuje pojedyńczą linijkę
        i+=1 #następuje podniesienie i
        if i % 5 == 0:
            try:
                o = input("press enter  to continue:")
            except:
                break

    
        
            