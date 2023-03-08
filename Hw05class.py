class CompanyEmployee:
    #def __init__(self,name,gender,age,salary):
    def __init__(self,name):
        self.name = name
        #self.gender = gender
        #self.age = age
        #self.salary = salary
    
    def hello(self):
        print("--------------------------------------------------------------------")
        print('ข้อมูลพนักงานบ.เย็นดี')
        print('คุณ',self.name)

class Accounting(CompanyEmployee):
    def __init__(self, name, gender, age, salary):
        super().__init__(name)
        self.gender = gender
        self.age = age
        self.salary = salary

    def personalinfo(self):
        
        print("แผนก: บัญชี\nเพศ : ",self.gender,"\nอายุ : ",self.age,"\nเงินเดิอน : ",self.salary)

class Electrician(CompanyEmployee):
    def __init__(self, name, gender, age, salary):
        super().__init__(name)
        self.gender = gender
        self.age = age
        self.salary = salary

    def personalinfo(self):
        
        print("แผนก: ช่างไฟ\nเพศ : ",self.gender,"\nอายุ : ",self.age,"\nเงินเดิอน : ",self.salary)

staff01 = Accounting("นินา","หญิง","30",18000)
staff01.hello()
staff01.personalinfo()
staff02 = Electrician("วิษณุ","ชาย","35",15000)
staff02.hello()
staff02.personalinfo()
staff03 = Accounting("นก","หญิง","28",16000)
staff03.hello()
staff03.personalinfo()