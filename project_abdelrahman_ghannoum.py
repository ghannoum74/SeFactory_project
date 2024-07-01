import tkinter
class User:
    def __init__(self, fullname, age, email, password, address, bio , hobit) -> None:
        self.fullname = fullname
        self.age = age
        self.email = email 
        self.password = password
        self.address = address 
        self.hobit = hobit
        self.bio = bio
        self.following = 0
        self.followers = 0
        self.block = 0
        self.isActive = False
        self.isAdmin = False

   