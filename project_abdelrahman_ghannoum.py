import tkinter
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
                    "email" : current.email,
                    "password" : current.password,
                    "address" : current.address,
                    "hobits" : current.hobits,
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
#parent component
        window = tkinter.Tk()
#title for my GUI program
        window.title("Friendship Community")
#nested component in my window
        frame = tkinter.Frame(window)
#to save my frame
        frame.pack()
#to run my window component
        window.mainloop()

