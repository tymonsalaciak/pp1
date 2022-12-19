class Student():

    uni = "UEK Kraków"

    id = 100000

    def __init__(self,name, surname,fof_study):
        self.name = name
        self.surname = surname
        Student.id += 1
        self.id = Student.id
        #Student.id += 1
        self.fof_study = fof_study

    def __str__(self):
        return f"{self.name} {self.surname}({self.id}), {self.fof_study}, {Student.uni}"

#Anna MAJ (100001), Applied Informatics, UEK Kraków

                    
a = Student("Tymon","WWW", "Applied Informatics")
print(a)

d = Student("Tymon","WWW", "Applied Informatics")
print(d)

s = Student("Tymon","WWW", "Applied Informatics")
print(s)