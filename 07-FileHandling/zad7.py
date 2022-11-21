# display text file, line by line

file = open('countries.txt','r')
file_content = file.read()




for line in file_content:
     #x = file_content.count(line)
     #print(x)
     print(line, end="")
file.close()