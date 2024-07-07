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
        with open("userDB.json", 'r') as file:
            users_data = json.load(file)
        users_data[destinationuser['email']] = destinationuser
        with open('userDB.json', 'w') as file :
            json.dump(users_data, file)
        
        
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
            friends = []
            current = self.head
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
    #so when i exit this program and comeback i will not use these data
        # with open("userDB.json", "r") as file:
        #     all_users = json.load(file)
        # for user in all_users:
        #     self.adj_list[user] = FriendsList()

    #add new user to the adj_list
    def register(self, user):
    #i used this algorith in the setUserData in
        if user['email'] not in self.adj_list:
            self.adj_list[user['email']] = FriendsList()
            self.loadUser(user)
            return True
        else :
            return False
        
    def displayFriendList(self):
        
        if self.adj_list == {}:
            print("Graph is empty!\n")
        else :
            for vertex in self.adj_list:
                friends = self.adj_list[vertex].displayFriends()
                print(vertex + ":", friends if friends else "No friends :(")
        
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

    def login(self, email, password):
        with open('userDB.json', 'r') as file:
            users = json.load(file)
        if email in users:
            if password == users[email]['password']:
        #set is active true
                users[email]['isActive'] = True
        #return data for user
                return users[email]
            else:
                return False
        else:
            return False

    def loadUser(self, user_data):
        with open("userDB.json", 'r') as file:
            users_data = json.load(file)
        users_data[user_data['email']] = user_data
        with open('userDB.json', 'w') as file :
            json.dump(users_data, file)