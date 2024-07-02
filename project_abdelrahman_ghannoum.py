import re
import tkinter
import tkinter.messagebox
import requests
from tkinter import ttk
from tkinter import messagebox
class UserNode:
    def __init__(self,friendsData) -> None:
        self.fullname = friendsData["fullname"]
        self.age = friendsData["age"]
        self.gender = friendsData["gender"]
        self.email = friendsData["email"] 
        self.password = friendsData["password"]
        self.nationality = friendsData["nationality"] 
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
                    "nationality" : current.nationality,
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
        frame = tkinter.Frame(window, padx=20, pady= 20)
#to save my frame
        frame.pack(padx=100, pady=100)

        ##################################################
        #                 handleForm fct                 #
        ##################################################

        def handleForm():
        ##################################################
        #                 Error handling                 #
        ##################################################
            if not re.match("^(?=.{3,}$)[a-zA-Z]+( [a-zA-Z]+)?$", full_name_input.get()):
                tkinter.messagebox.showerror(title="fullname Error" , message="fullname not acceptable . it should not contain any spetial characteres (/*@#$) or numbers(0--->9) and should contain at least 3 characteres")
            elif gender_combobox.get()!= "Male" or gender_combobox.get()!= "Female" or gender_combobox.get()!= "rather not say":
                  tkinter.messagebox.showerror(title="Gender Error", message="Gender should be one from the list")
            elif not nationality_input.get() :
                  tkinter.messagebox.showerror(title="Nationality Error", message="Nationality field required")
            elif not re.match("^[a-zA-Z0-9._%+-]+@(gmail\\.com|hotmail\\.com|[a-zA-Z0-9.-]+\\.(co|com))$", email_input.get()):
                tkinter.messagebox.showerror(title="Email Error", message="Email should be as format : Example123@exmail.co")
            elif not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*])[A-Za-z\\d!@#$%^&*]{8,}$", password_input.get()):
                tkinter.messagebox.showerror(title="Password Error", message="strong password should contain Minimum 8 characters. At least one uppercase letter. At least one lowercase letter. At least one number. At least one special character (e.g., !@#$%^&*).")
            else :
                acceptedTerms = term_var.get()
                if acceptedTerms == "1":
                    friend_data = {
                    "fullname" : full_name_input.get(),
                    "age" : age_spinbox.get(),
                    "gender" : gender_combobox.get(),
                    "email" : email_input.get(),
                    "password" : password_input.get(),
                    "nationality" : nationality_input.get(),
                    "hobits" : hobits_input.get(),
                    "bio" : bio_input.get(),
                    "term & policie":term_var.get()
                    }
                    print(friend_data)
                else:
                    tkinter.messagebox.showwarning(title="fullname Error", message="terms & policy should be accepted")
            

        ##################################################
        #           start by Personal info               #
        ##################################################

#saving personal info
        personal_info_frame = tkinter.LabelFrame(frame, text= "Personal_Information")
        personal_info_frame.grid(row=0 , column= 0 ,padx=10, pady=10)

#create full_name label , inputs and render it
        full_name_label = tkinter.Label(personal_info_frame, text="Full name")
        full_name_input = tkinter.Entry(personal_info_frame)
        full_name_label.grid(row = 0, column = 0)
        full_name_input.grid(row = 1, column= 0)
#create hobits_label , inputs and render it
        hobits_label = tkinter.Label(personal_info_frame, text="Hobits")
        hobits_input = tkinter.Entry(personal_info_frame)
        hobits_label.grid(row = 0, column = 1)
        hobits_input.grid(row = 1, column= 1)
#create bio_label , input and render it 
        bio_label = tkinter.Label(personal_info_frame, text="Bio")
        bio_input = tkinter.Entry(personal_info_frame)
        bio_label.grid(row = 0, column = 2)
        bio_input.grid(row = 1, column= 2)
#create gender label , inputs and render it
        gender = tkinter.Label(personal_info_frame, text="Gender")
        gender_combobox = ttk.Combobox(personal_info_frame, values=["Male", "Female", "rather not say"])
        gender.grid(row= 2, column= 0 )
        gender_combobox.grid(row=3, column= 0)
#create age_label, input and render it
        age_label = tkinter.Label(personal_info_frame, text="Age")
        age_spinbox = tkinter.Spinbox(personal_info_frame, from_=12 , to= 90)
        age_label.grid(row=2 , column=1)
        age_spinbox.grid(row=3, column=1)
#create nationality label, input fetching and render it
        nationality_label = tkinter.Label(personal_info_frame, text="Nationality")
####fetching nationality api####
        req = requests.get("https://freetestapi.com/api/v1/countries")
        response =[county["name"] for county in req.json()[:150]]
        nationality_input = ttk.Combobox(personal_info_frame,values=response)
        nationality_label.grid(row=2, column=2)
        nationality_input.grid(row= 3, column= 2)

#set padding for personal inputs
        for wedget in personal_info_frame.winfo_children():
            wedget.grid_configure(padx=10, pady= 5)

        ##################################################
        #           start by account info                #
        ##################################################

        account_info_frame = tkinter.LabelFrame(frame, text= "Account_Information")
        account_info_frame.grid(row=1 , column= 0,sticky="news",padx=10, pady=10)
#create email label , inputs and render it
        email_label = tkinter.Label(account_info_frame, text="Email")
        email_input = tkinter.Entry(account_info_frame)
        email_label.grid(row = 2, column = 1)
        email_input.grid(row = 3, column= 1)
#create password_label , inputs and render it
        password_label = tkinter.Label(account_info_frame, text="Password")
        password_input = tkinter.Entry(account_info_frame)
        password_label.grid(row = 2, column = 2)
        password_input.grid(row = 3, column= 2)
#create show_password_btn_label , inputs and render it
        show_password_btn_label = tkinter.Checkbutton(account_info_frame, text="show Password")
        show_password_btn_label.grid(row = 3, column = 4)

#set padding for personal inputs
        for wedget in account_info_frame.winfo_children():
            wedget.grid_configure(padx=10, pady= 5)

        ##################################################
        #           start by terms & conditions info     #
        ##################################################

        terms_conditions_frame = tkinter.LabelFrame(frame, text= "Terms & Conditions")
        terms_conditions_frame.grid(row=2 , column= 0,sticky="news",padx=10, pady=10)
#create terms_btn_label , inputs and render it
        term_var = tkinter.StringVar(value=False)
        terms_btn_label = tkinter.Checkbutton(terms_conditions_frame, text="Accept all terms and conditions", variable=term_var, onvalue=True,offvalue=False)
        terms_btn_label.grid(row = 0, column = 0)        

        ##################################################
        #                 start by button                #
        ##################################################
        button = tkinter.Button(frame, text="Submit" , command= handleForm)
        button.grid(row = 3, column=0, sticky="news",padx=10, pady=10)

#to run my window component
        window.mainloop()

def main():
    friend = FriendshipCommunity()
    friend.createUser()
main()
    