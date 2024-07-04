# from addNewUser import addUser
from newUserClass import newUSer
class UserNode:
    def __init__(self, email) -> None:
        # self.fullname = friendsData["fullname"]
        # self.age = friendsData["age"]
        # self.gender = friendsData["gender"]
        # self.password = friendsData["password"]
        # self.nationality = friendsData["nationality"] 
        # self.hobbies= friendsData["hobbies"]
        # self.bio = friendsData["bio"]
        self.email = email
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
        print(f"{friendData} has been added successfuly")
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
        
    #i already managed the existence user in the addUser()function so all user is not existe in the self.adj_list
    #this is like temparary data base when we enter the user GUI you can add as match as you want user and it managed if user entered twice 
    #when you print exit all users entered is passed to user object and store it in the adj_list dictionary
    #so now i retrive each user (email) and set it as vertex with value equal to empty FriendList[linledlist]
        users_email = list(user.user_data.keys())
        for email in users_email:
            self.adj_list[email] = FriendsList()

    
    def follow(self, sourceUser, destinationUser):
        if sourceUser in self.adj_list and destinationUser in self.adj_list:
            self.adj_list[sourceUser].addFriend(destinationUser)
            print(f"You are now friend with {destinationUser}")
        elif sourceUser not in self.adj_list and destinationUser not in self.adj_list:
            print("Invalid", sourceUser,"and",destinationUser)
        elif sourceUser not in self.adj_list:
            print("Invalid", sourceUser)
        elif destinationUser not in self.adj_list:
            print("Invalid",destinationUser)

    def display(self):
        if self.adj_list == {}:
            print("Graph is empty!\n")
            return
        for vertex in self.adj_list:
            friends_str = self.adj_list[vertex].displayFriends()
            print(f"{vertex}: {friends_str}")

    

        

def main():
    friend = FriendshipCommunity()
    friend.createUser()
    friend.follow("aboud1@gmail.com", "aboud2@gmail.com")
main()
    