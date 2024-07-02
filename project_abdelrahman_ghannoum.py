import tkinter
import json
class UserNode:
    def __init__(self,friendsData) -> None:
        self.fullname = friendsData["fullname"]
        self.age = friendsData["age"]
        self.email = friendsData["email"] 
        self.password = friendsData["password"]
        self.address = friendsData["address"] 
        self.hobits = friendsData["hobits"]
        self.bio = friendsData["bio"]
        self.following = 0
        self.followers = 0
        self.block = 0
        self.isActive = False
        self.isAdmin = False
        pass
#It's our linked list for the friends of vertesis
class FriendsList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

#it's the same as addnode
    def addFriend(self, friendData):
        friend = UserNode(friendData)
        friend.next = self.head
        self.head = friend
        print(f"{friendData["fullname"] } has been added successfuly")
        self.size += 1

#it's the same as removeNode
    def removeFriend(self, friend):
        if self.size == 0:
            print("You're Lonely . You don't even have a friends to remove it :(")
            return
        elif self.head.email == friend:
            self.head = self.head.next
            self.size -= 1
            print(f"{friend} removed")
        else :
            current = self.head.next
            previous = self.head
            while current :
                if current.email == friend:
                    previous.next = current.next
                    self.size -= 1
                    print(f"{friend} removed")
                    return 
                previous = current 
                current = current.next
            print(f"Friend {friend} not found in the list.")
                

def main():
    user = FriendsList()
    friendData = {"fullname":"ahmad","age":16,"email":"ahmad123@gmail.com", "password":"ahmad123","address": "adhidhdkd","hobits" :"fdkjh" ,"bio": "dsahfaiufjkfe"}
    user.addFriend(friendData)
main()
    

   