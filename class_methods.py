class User:
    
    active_users = 0

    # class methods:
# i) denoted with the help of decorator
# ii) not concerned with specific intances but with the class itself
    @classmethod
    def display_active_users(cls):
        return f"there are currently {cls.active_users}"

    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))
    
    def __init__(self,first,last,age):
        self.first = first  # instance attributes
        self.last = last
        self.age = age
        User.active_users += 1
    
    def logout(self):
        User.active_users -=1;
        return f"{self.first} has logged out"

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
    

# print(User.active_users)
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# # print(User.active_users)
# # print(user2.logout)

# print(User.display_active_users())

# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())
    
tom = User.from_string("Tom,Jerry,64")
print(tom.first)
print(tom.full_name())
print(tom.birthday())