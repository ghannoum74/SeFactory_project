# from addNewUser import addUser
from newUserClass import newUSer
class UserNode:
    def __init__(self,friendsData) -> None:
        self.fullname = friendsData["fullname"]
        self.age = friendsData["age"]
        self.gender = friendsData["gender"]
        self.email = friendsData["email"] 
        self.password = friendsData["password"]
        self.nationality = friendsData["nationality"] 
        self.hobbies= friendsData["hobbies"]
        self.bio = friendsData["bio"]
        self.following = 0
        self.followers = 0
        self.block = 0
        self.isActive = False
        self.isAdmin = False
        self.next = None
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
            print(f"{self.head.fullname} removed")
            self.head = self.head.next
            self.size -= 1
        else :
            current = self.head.next
            previous = self.head
            while current :
                if current.email == friend:
                    previous.next = current.next
                    self.size -= 1
                    print(f"{current.fullname} removed")
                    return 
                previous = current 
                current = current.next
            print(f"{friend} not found in the list.")
                
    def getSize(self):
        print(f"Your have {self.size} followers")

    def displayFriends(self):
        if self.size == 0:
            print("list is empty")
        else:
            current = self.head
            friends = []
            while current :
                friend_data = {
                    "fullname" : current.fullname,
                    "age" : current.age,
                    "gender" : current.gender,
                    "email" : current.email,
                    "password" : current.password,
                    "nationality" : current.nationality,
                    "hobbies" : current.hobbies,
                    "bio" : current.bio,
                }
                friends.append(friend_data)
                current = current.next
            print(friends)

##################################################
class FriendshipCommunity:
    def __init__(self) -> None:
        self.adj_list = {}

    def createUser(self):
        user = newUSer()
        user.addUser()
        if user.getUserData():
            print(user.user_data)
            # print(user.getUserData())
            # if user.getUserData()["email"] not in self.adj_list:
            #     self.adj_list[user.getUserData()["email"]] = FriendsList()
            #     print("user", user, "has been added!\n")
            #     print(self.adj_list)
            #     return 
            # print("user ", user.getUserData()["email"], "already exists!\n")
        else :
            print("No user get it from the form")

        

def main():
    friend = FriendshipCommunity()
    friend.createUser()
    
main()
    