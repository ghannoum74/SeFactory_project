import json
# from addNewUser import addUser
from newUserClass import newUSer
class UserNode:
    
    def __init__(self, friendsData) -> None:
        self.fullname = friendsData["fullname"]
        self.age = friendsData["age"]
        self.gender = friendsData["gender"]
        # self.password = friendsData["password"]
        self.nationality = friendsData["nationality"] 
        self.hobbies= friendsData["hobbies"]
        self.bio = friendsData["bio"]
        self.email = friendsData["email"]
        self.following_list = friendsData["following_list"]
        self.followers_list = friendsData["followers_list"]
        self.following = friendsData["following"]
        self.followers = friendsData["followers"]
        self.isActive = friendsData["isActive"]
        self.block = 0
        self.isAdmin = False
        self.next = None
        pass

    def addFollowing(self):
        self.following += 1

    def addFollowers(self, user):
        user.followers +=1

#It's our linked list for the friends of vertesis
class FriendsList:
    def __init__(self) -> None:
        self.head = None
        self.size= 0

#it's the same as addnode
    def addFriend(self, destinationuser):
    #get data from database
        with open("userDB.json", "r") as file:
            all_users = json.load(file)
    
    #get data for specific user the destinationuser
        user = all_users[destinationuser]
    #creation successfuly
        friend = UserNode(user)
    #add friend to the its own destinationuser_list 
        friend.addFollowing()
    #add node to linked list 
        friend.next = self.head
        self.head = friend
    #save to DB the change
        print(f"{user['fullname']} has been added successfuly")
        self.size += 1

    #return new data to DB
        with open("userDB.json", "w") as file:
           json.dump(all_users, file, indent=4)
        
#it's the same as removeNode
    def removeFriend(self, friend):
        if self.size== 0:
            print("You're Lonely . You don't even have a friends to remove it :(")
            return
        elif self.head.email == friend:
            print(f"{self.head.fullname} removed")
            self.head = self.head.next
            self.size-= 1
        else :
            current = self.head.next
            previous = self.head
            while current :
                if current.email == friend:
                    previous.next = current.next
                    self.size-= 1
                    print(f"{current.fullname} removed")
                    return 
                previous = current 
                current = current.next
            print(f"{friend} not found in the list.")
                
    def getSize(self):
        print(f"Your have {self.followers} followers")


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
                    # "password" : current.password,
                    "nationality" : current.nationality,
                    "hobbies" : current.hobbies,
                    "bio" : current.bio,
                    "following": current.following,
                    "followers": current.followers,
                    "isActive": current.isActive,
                    "following_list": current.following_list,
                    "followers_list": current.followers_list
                }
                friends.append(friend_data)
                current = current.next
            return friends

##################################################
class FriendshipCommunity:
    def __init__(self) -> None:
        self.adj_list = {}

    #initial self.adj_list by all the users in the DB
        with open("userDB.json", "r") as file:
            all_users = json.load(file)
        for user in all_users:
            self.adj_list[user] = FriendsList()
        

    def createUser(self):
        user = newUSer()
        user.addUser()
    #i didn't handle if user in self.adj_list because im sure that the data base dosent contain any same users
        with open("userDB.json", "r") as file:
            all_users = json.load(file)

        for user in all_users:
            self.adj_list[user] = FriendsList()
    
    def follow(self, sourceUser, destinationUser):
        with open("userDB.json", "r") as file:
            all_users = json.load(file)
        
        if sourceUser in self.adj_list and destinationUser in self.adj_list:
            self.adj_list[sourceUser].addFriend(destinationUser)
            print(f"You are now friend with {destinationUser}")
        elif sourceUser not in self.adj_list and destinationUser not in self.adj_list:
            print("Invalid", sourceUser,"and",destinationUser)
        elif sourceUser not in self.adj_list:
            print("Invalid", sourceUser)
        elif destinationUser not in self.adj_list:
            print("Invalid",destinationUser)

    def displayFriendList(self):
        
        if self.adj_list == {}:
            print("Graph is empty!\n")
            return
        else :
            for vertex in self.adj_list:
                print(vertex + ":", self.adj_list[vertex].displayFriends())
        

def main():
    friend = FriendshipCommunity()
    # friend.createUser()
    friend.follow("aboud2@gmail.com","ghann1@gmail.com")
    # friend.follow("aboud2@gmail.com","ghannoum8@gmail.com")
    # friend.follow("aboud2@gmail.com","ghann1@gmail.com")
    friend.displayFriendList()
    # friend.follow("abo2@gmail.com","gha9@gmail.com")
    # friend.follow("abou@gmail.com","ghann1@gmail.com")
    # friend.follow("aboud2@gmail.com","ghann2@gmail.com")
    # friend.displayFriendList()
main()
    

        

    