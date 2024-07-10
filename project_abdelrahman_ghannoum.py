import json
import networkx as nx
import matplotlib.pyplot as plt

class UserNode:
    
    def __init__(self, friendsData) -> None:
        self.fullname = friendsData["fullname"]
        self.age = friendsData["age"]
        self.gender = friendsData["gender"]
        self.password = friendsData["password"]
        self.nationality = friendsData["nationality"] 
        self.hobbies= friendsData["hobbies"]
        self.bio = friendsData["bio"]
        self.email = friendsData["email"]
        self.friend_list = friendsData["friend_list"]
        self.friend_count = friendsData['friend_count']
        self.isActive = friendsData["isActive"]
        self.block = 0
        self.isAdmin = False
        self.next = None
        pass
    
#It's our linked list for the friends of vertesis
class FriendsList:
    def __init__(self) -> None:
        self.head = None
        self.size= 0

    #checking before addFriend if friend(new node) is already exust in the LinkedList for the user log in
    def checkingFriend(self, friend):
        current = self.head
        while current:
            if friend.email == current.email:
                return True
            current = current.next
        return False
    
#it's the same as addnode
    def addFriend(self,sourceUser, destinationUser):
    #creation successfuly
        friend = UserNode(destinationUser)
        result = self.checkingFriend(friend)
        
        if not result:
        #add to friend list
            result = self.addToFriendList(sourceUser, destinationUser)
            #add node to linked list 
            friend.next = self.head
            self.head = friend
            print(f"{destinationUser['fullname']} has been added successfuly")
            self.size += 1


        #add friend to friend_list for the source and increment following by 1
            self.loadData(sourceUser['email'], result)
        else :
           return True
    
        
#it's the same as removeNode
    def removeFriend(self,sourceUser , friend_email):
        if self.size== 0:
            print("You're Lonely . You don't even have a friends to remove it :(")
            return
        elif self.head.email == friend_email:
            print(f"{self.head.fullname} removed")
            self.head = self.head.next
            self.size-= 1
            with open('userDB.json', 'r') as file :
                users_data = json.load(file)
            del users_data[sourceUser['email']]['friend_list'][friend_email]
            with open('userDB.json', 'w') as file :
                json.dump(users_data, file)
            print(users_data[sourceUser['email']]['friend_list'], "----------------------------------")
            # users_data[sourceUser]['friend_list'].remove(friend_email)
            return True
        else :
            current = self.head.next
            previous = self.head
            while current :
                if current.email == friend_email:
                    previous.next = current.next
                    self.size-= 1
                    print(f"{current.fullname} removed")
                    with open('userDB.json', 'r') as file :
                        users_data = json.load(file)
                    del users_data[sourceUser['email']]['friend_list'][friend_email]
                    with open('userDB.json', 'w') as file :
                        json.dump(users_data, file)
                    
                    return True
                previous = current 
                current = current.next
            return False
            print(f"{friend} not found in the list.")
                

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
                    "friend_count": current.friend_count,
                    "isActive": current.isActive,
                    "friend_list": current.friend_list,
                }
                friends.append(friend_data)
                current = current.next
            return friends
    
    def addToFriendList(self,sourceUser, destination):
    #add to (dictionary) followers list the source by key is the email of source and values sourceUser
    #self refere to destination
        sourceUser["friend_list"][destination['email']] = destination['email']
        sourceUser["friend_count"] = len(sourceUser["friend_list"])
        return [sourceUser["friend_list"], sourceUser["friend_count"]]

    def loadData(self, sourceUSer,  result_following):
        with open("userDB.json", 'r') as file:
            users_data = json.load(file)
        users_data[sourceUSer]['friend_list'] = result_following[0]
        users_data[sourceUSer]['friend_count'] = result_following[1]
        with open('userDB.json', 'w') as file:
            json.dump(users_data, file)
        
    def reloadRelations(self, destination):
        friend = UserNode(destination)
        friend.next = self.head
        self.head = friend
        print(f"{destination['fullname']} has been reload successfuly")
        self.size += 1
##################################################
class FriendshipCommunity:
    def __init__(self) -> None:
        self.adj_list = {}
    #initial self.adj_list by all the users in the DB
    #so when i exit this program and comeback i will not use these data
    #Note : i can hide this and start programe from biggining and add two users and only with this two i can add friend
        with open("userDB.json", "r") as file:
            all_users = json.load(file)
        for user in all_users:
            self.adj_list[user] = FriendsList()
            if all_users[user]['friend_list']:
                for follower_key, follower_data in all_users[user]['friend_list'].items():
                    self.adj_list[user].reloadRelations(all_users[follower_data])
                # else:
                    pass
        self.displayFriendList()

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
        #checking for email for source and destination exist
        if sourceUser['email'] in self.adj_list and destinationUser['email'] in self.adj_list:
    #handle if result = False
            result = self.adj_list[sourceUser['email']].addFriend(sourceUser, destinationUser)
            if result :
                return(f"You are already friend with {destinationUser['email']}")
            
            return(f"You are now friend with {destinationUser['email']}")
        
        elif sourceUser['email'] not in self.adj_list and destinationUser['email'] not in self.adj_list:
            return("Invalid", sourceUser['email'], "and", destinationUser['email'])
        
        elif sourceUser['email'] not in self.adj_list:
            return("Invalid", sourceUser['email'])
        
        elif destinationUser['email'] not in self.adj_list:
            return("Invalid",destinationUser['email'])

    def unfollow(self, sourceUser, destinationUser):
        result = self.adj_list[sourceUser['email']].removeFriend(sourceUser, destinationUser)
        self.displayFriendList()
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

    def dfsSearch(self, start_node, searching_by, searching_value, visited=None, result = None):
        if visited == None:
            visited = set()
        if result == None:
            result = {}
        visited.add(start_node)
        if start_node in self.adj_list:
            for neighbor_node in self.adj_list[start_node].displayFriends():
                if neighbor_node[searching_by] == searching_value and neighbor_node['email'] not in visited  :
                    
            #return values as dictionary because in my follow page i'm working with dictionary only
                    result[neighbor_node['email']] = neighbor_node
                    self.dfsSearch(neighbor_node['email'], searching_by, searching_value, visited, result)
        return result
    