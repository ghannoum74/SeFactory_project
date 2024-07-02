import tkinter
from tkinter import ttk
class UserNode:
    def __init__(self,friendsData) -> None:
        self.fullname = friendsData["fullname"]
        self.age = friendsData["age"]
        self.gender = friendsData["gender"]
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
                    "gender" : current.gender,
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
#saving user info
        user_info_frame = tkinter.LabelFrame(frame, text= "User_Information")
        user_info_frame.grid(row=0 , column= 0 )

#create full_name label
        full_name_label = tkinter.Label(user_info_frame, text="Full name")
#render label on the screen
        full_name_label.grid(row = 0, column = 0)
#create the input for full_name label
        full_name_input = tkinter.Entry(user_info_frame)
#render input on the screen
        full_name_input.grid(row = 1, column= 0,padx=20,pady=20)
#create gender label
        gender = tkinter.Label(user_info_frame, text="Gender")
#render label
        gender.grid(row= 0, column= 2 )
#create combobox
        gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "rather not say"])
#render combobox
        gender_combobox.grid(row=1, column= 2)
#create age_label
        age_label = tkinter.Label(user_info_frame, text="Age")
#render age_label
        age_label.grid(row=0 , column=3)
#create age spinbox
        age_spinbox = tkinter.Spinbox(user_info_frame, from_=12 , to= 90)
#render age spinbox
        age_spinbox.grid(row=1, column=3)
#create address label
        address_label = tkinter.Label(user_info_frame, text="Address")
#render address label
        address_label.grid(row=2, column=0)
#create address input
        address_input = tkinter.Entry(user_info_frame)
#render address input
        address_input.grid(row=3, column=0)
#to run my window component
        window.mainloop()

def main():
    friend = FriendshipCommunity()
    friend.createUser()
main()
