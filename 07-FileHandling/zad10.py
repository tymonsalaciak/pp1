file = open('file.txt','w',encoding="utf-8")
file_content = file.write("Tymon Sałaciak, UEK\n") #, end="\n" write nie przyjmuje drugiego argumentu
file_content = file.write("informatyka stosowana ")
file.close()