import tkinter
import json
class UserNode:
    def __init__(self,fullname, age, email, password, address, hobits, bio) -> None:
        self.fullname = fullname
        self.age = age
        self.email = email 
        self.password = password
        self.address = address 
        self.hobits = hobits
        self.bio = bio
        self.following = 0
        self.followers = 0
        self.block = 0
        self.isActive = False
        # self.isAdmin = False
        pass
#It's our linked list for the friends of vertesis
class FiendsList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def addFriend(self, friendData):
        friend = UserNode(friendData)
        friend.next = self.head
        self.head = friend
        self.size += 1


    

   