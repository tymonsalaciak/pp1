"""
f = open("filename.txt", "r", encoding="utf-8")
for line in f:
     print(line, end="")
f.close()
"""
with open("filename.txt", "r", encoding="utf-8") as fil:
    for line in fil:
     print(line, end="")
