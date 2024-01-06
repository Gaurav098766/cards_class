class User:
    def __init__(self,first,last,age):
        self.first = first  # instance attributes
        self.last = last
        self.age = age
    
    def full_name(self): # instance methods
        return self.first + " " + self.last
 
    def initials(self):
        return self.first[0]+" "+self.last[0]

    def likes(self,thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age +=1
        return f"Happy {self.age}th, {self.first}"

user = User("Gaurav","Sharma",23)
print(user.first,user.last)
print(user.full_name())
print(user.initials())

user1 = User("Joe","Smith",58)
user2 = User("Blanca", "Lopez", 41)
print(user2.is_senior())
print(user1.birthday())
print(user1.age)


class Comment:
    def __init__(self,username,text,likes=0):
        self.username = username
        self.text = text
        self.likes = likes

# Dunder Methods:
# __xyz__ : this is some build in methods in pyhton so u cant define your own.
# _xyz: this is a convention to tell developer that this is suppoed to private methods or attribute
#         and if it is not supposed to be used outside the class.
# __xyz: (known as name mangline) 


class BankAccount:
    def __init__(self,name):
        self.owner = name
        self.balance =0.0

    def getBalance(self):
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self,amount):
        self.balance +=amount
        return self.balance