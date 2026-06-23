# class Student:
#     def __init__(self, name, grade, percentage, team):
#         self.name = name
#         self.grade = grade
#         self.percentage = percentage
#         self.__team = team
#     def get_team():
#         return __team
#     def info(self):  #Abstraction method <>
#         print(f"{self.name} is in grade {self.grade} with {self.percentage+2}% from team {self.team}") #Hidden from users

# team1 = "A"
# team2 = "B"
# student1 = Student("raghav", "B", 57, team2)
# student2 = Student("aryan", "A", 98, team1)






# # Program I

# class Student:
#     def __init__(self, name , sub1, sub2, sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#     def get_avg(self):
#         average = (self.sub1+self.sub2+self.sub3)/3
#         return average

# student1 = Student("aryan", 45, 34, 12)
# print(student1.__dict__)

# print(student1.get_avg())


# # Program II

class Account:
    def __init__(self, balance, accountnumber):
        self.balance = balance
        self.__accountnumber = accountnumber
    def get__accountnumber(self):
        return self.__accountnumber
    def debit(self, amount):
        self.balance-=amount
        print("rs.", amount, "was debited")
    def credit(self, amount):
        self.balance+=amount
        print("rs.", amount, "was credited")
    def get_balance(self):
        total_balance = f"Total balance = {self.balance}"
        return total_balance
        
account1 = Account(10000, 321)
account1.debit(500)
account1.credit(300)
print(account1.get_balance())
print(account1.get__accountnumber())

# Inheritence

# class Vehicle:

#     @staticmethod
#     def start():
#         print("Started...")
#     @staticmethod
#     def end():
#         print("Ended...")
    

# class Car():
#     tyre = "black leather"
#     color = "black"

# class Fortuner(Vehicle, Car):
#     name = "fortuner"
#     brand = "toyota"
#     manufacture = "india"


# fortuner1 = Fortuner()
# fortuner1.start()
# print(fortuner1.brand)
# print(fortuner1.color)
# print(fortuner1.name)
# fortuner1.end()

# # Program III

# class Employee:
#     company = "XYZ institude"
#     def __init__(self, name, phy, chem, math):
#         self.name = name
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
#     def per(self):
#         sum = (self.phy+self.chem+self.math)/3
#         return f"{sum}%"

# e1 = Employee("prince", 65, 76, 98)
# print(e1.name)
# e1.chem = 76
# print(e1.per())