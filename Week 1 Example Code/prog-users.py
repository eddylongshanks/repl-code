
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def details(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) +"\n"
    
    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) +"\n"
    
    def __repr__(self):
        return "User(name, age)"

# Inherit from User
class Admin(User):
    def details(self):
        return "Name: " + self.name + " (Admin)\nAge: " + str(self.age) +"\n"

    # __str__ will return this line when calling the class. eg: print(user1)
    def __str__(self):
        return "Name: " + self.name + " (Admin)\nAge: " + str(self.age) +"\n"
    
    def __repr__(self):
        return "Admin(User)"

class Users:
    def __init__(self):
        self.users = []
    
    def AddUser(self, user):
        # Check for the type of the object to determine admin status
        if user is type(Admin):
            user = Admin(user.name, user.age)
        elif user is type(User):
            user = User(user.name, user.age)
        self.users.append(user)
    
    def GetUsers(self):        
        print("There are {0} users\n".format(str(len(self.users))))
        for user in self.users:
            print(user.details())
    
    def __str__(self):
        return "There are {0} users\n".format(str(len(self.users)))

    def __repr__(self):
        return "Users()"

users = Users()
numberOfUsers = int(input("How many users do you want to add?: "))
userCount = 1

while userCount <= numberOfUsers:
    name = input("What is the name of user " + str(userCount) + "?: ")
    age = input("What is the age of user " + str(userCount) + "?: ")
    # Create a new user with the accepted information
    currentUser = User(name, age)
    # Add new user to the list
    users.AddUser(currentUser)
    userCount += 1

# Create an admin user and add to the list
admin = Admin("Chris", 30)
users.AddUser(admin)

# List the current users
users.GetUsers()





