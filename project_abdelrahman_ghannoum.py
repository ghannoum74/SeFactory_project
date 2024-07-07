import json
# from addNewUser import addUser

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
        # self.following_list.append(friend_email)

    def addFollowers(self):
        self.followers +=1

    def addToFollowersList(self, followingUser):
        self.followers_list[followingUser] = followingUser

#It's our linked list for the friends of vertesis
class FriendsList:
    def __init__(self) -> None:
        self.head = None
        self.size= 0

#it's the same as addnode
    def addFriend(self,destinationuser, sourceuser):
    #creation successfuly
        friend = UserNode(destinationuser)
    #add friend to the its own destinationuser_list 
        friend.addFollowers()
        friend.addToFollowersList(sourceuser['email'])
    #add node to linked list 
        friend.next = self.head
        self.head = friend
    #save to DB the change
        print(f"{destinationuser['fullname']} has been added successfuly")
        self.size += 1
    #update  data to DB
        with open('userDB.json', 'r+') as file:
            user = json.load(file)
            user[destinationuser['email']] = destinationuser
    #to move the pointer to beginning
            file.seek(0) 
            json.dump(user, file, indent=4)
        
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
        
    #add new user to the adj_list
    def createUser(self):
        pass

    #     #no need to manage if user exist because i already managed in my GUI
    #     self.adj_list[user] = FriendsList()
    
    def follow(self, sourceUser, destinationUser):
        with open("userDB.json", "r") as file:
            all_users = json.load(file)
        
        #checking if email for source and destination because with email vertesis are stored
        if sourceUser['email'] in self.adj_list and destinationUser['email'] in self.adj_list:
            self.adj_list[sourceUser['email']].addFriend(destinationUser, sourceUser)
            return(f"You are now friend with {destinationUser['email']}")
        
        elif sourceUser['email'] not in self.adj_list and destinationUser['email'] not in self.adj_list:
            return("Invalid", sourceUser['email'], "and", destinationUser['email'])
        
        elif sourceUser['email'] not in self.adj_list:
            return("Invalid", sourceUser['email'])
        
        elif destinationUser['email'] not in self.adj_list:
            return("Invalid",destinationUser['email'])

    def displayFriendList(self):
        
        if self.adj_list == {}:
            print("Graph is empty!\n")
            return
        else :
            for vertex in self.adj_list:
                print(vertex + ":", self.adj_list[vertex].displayFriends())
        

# def main():
#     friend = FriendshipCommunity()
#     friend.createUser()
#     # friend.follow({ "fullname": "aboud", "age": "13", "gender": "Female", "email": "aboud1@gmail.com", "password": "Aboud123!", "nationality": "Algeria", "hobbies": "", "bio": "", "term_policie": "1", "followers": 0, "following": 0, "isActive": 0, "followers_list": {}, "following_list": {}
#     # },{
#     #     "fullname": "aboud",
#     #     "age": "13",
#     #     "gender": "Female",
#     #     "email": "aboud2@gmail.com",
#     #     "password": "Aboud123!",
#     #     "nationality": "Algeria",
#     #     "hobbies": "",
#     #     "bio": "",
#     #     "term_policie": "1",
#     #     "following": 0,
#     #     "followers": 0,
#     #     "isActive": 0,
#     #     "followers_list": {
#     #         "aboud3@gmail.com": "aboud3@gmail.com"
#     #     },
#     #     "following_list": {}
#     # },)
#     # friend.follow("aboud2@gmail.com","ghannoum8@gmail.com")
#     # friend.follow("aboud2@gmail.com","ghann1@gmail.com")
#     # friend.displayFriendList()
#     # friend.follow("abo2@gmail.com","gha9@gmail.com")
#     # friend.follow("abou@gmail.com","ghann1@gmail.com")
#     # friend.follow("aboud2@gmail.com","ghann2@gmail.com")
#     # friend.displayFriendList()
# main()
    

        

    