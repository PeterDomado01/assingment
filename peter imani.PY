class registration:
    def __init__(self,name,reg_no,course,year):
        self.name=name
        self.reg_no=reg_no
        self.course=course
        self.year=year

    def __str__(self):
        return(f"name:{self.name} reg_no:{self.reg_no} course:{self.course} year:{self.year}")

student1=registration("john doe","S23B13/109","bcds","2023")
print(student1)    

student1=registration("marvin Mubiru","S23B14/100","law","2022")
print(student1) 

student1=registration("Nantongo sumayiya","S23B13/023","Law","2024")
print(student1)    

student1=registration("Mann Boy","S23B13/197","Bscs","2020")
print(student1)    
       
        