import tkinter
import re 
import requests
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox 
import json
from project_abdelrahman_ghannoum import FriendshipCommunity
class NewUser:
    def __init__(self) -> None:
        self.fullname_input = ""
        self.hobbies_input= None
        self.bio_input = None
        self.age_spinbox = ""
        self.gender_combobox = ""
        self.nationality_input = ""
        self.email_input = ""
        self.password_input = ""
        self.term_var = False   
        self.isActive = False

    #fetching data for nationality list
        self.countries_data = [county["name"] for county in requests.get("https://freetestapi.com/api/v1/countries").json()]

    #variable declared for toggling password input value from "*" to actual value
        self.show_password_toggle = ""

    # i used dictionary to store data to O(1) be the TC when i will iterable through the entire dictionary in set fuction and others
        self.user_data = {}
        #parent component
        self.root = tkinter.Tk()
        self.add_user_frame = tkinter.Frame(self.root, padx=20, pady= 20)

    #for login page
        self.login_frame = tkinter.Frame(self.root, padx=20, pady= 20)
        self.email_login = ""
        self.password_login = ""

    #for profile page
        # self.profile_page_frame = tkinter.Frame(self.root, padx=20, pady= 20)

    #create instance to use it in my all class
    # i create it here not in the setData function because when i want to add many vetex i want all these data store it in one instance which is this
    # not for each calling for new setData create new instance
    # this how i can check if vertex added is already exist or not 
        self.friend = FriendshipCommunity()
        ##################################################
        #                 create new user                #
        ##################################################

    def addUser(self):
    #title for my GUI program
        self.root.title("Friendship Community")
    #nested component in my window
        self.root.configure(bg="#ececec")
        self.add_user_frame = tkinter.Frame(self.root, padx=20, pady= 20)
        self.add_user_frame.configure(bg="#eeeeee")
        #to save my frame
        self.add_user_frame.grid(row=0 , column=0,padx=500, pady=170)
        
        ##################################################
        #           start by Personal info               #
        ##################################################

    #saving personal info
        personal_info_frame = tkinter.LabelFrame(self.add_user_frame, text= "Personal_Information")
        personal_info_frame.grid(row=0 , column= 0 ,padx=10, pady=10)

    #create full_name label , inputs and render it
        full_name_label = tkinter.Label(personal_info_frame, text="Full name")
        self.fullname_input = tkinter.Entry(personal_info_frame)
        full_name_label.grid(row = 0, column = 0)
        self.fullname_input.grid(row = 1, column= 0)
    #create hobbies_label , inputs and render it
        hobbies_label = tkinter.Label(personal_info_frame, text="Hobies")
        self.hobbies_input= tkinter.Entry(personal_info_frame)
        hobbies_label.grid(row = 0, column = 1)
        self.hobbies_input.grid(row = 1, column= 1)
    #create bio_label , input and render it 
        bio_label = tkinter.Label(personal_info_frame, text="Bio")
        self.bio_input = tkinter.Entry(personal_info_frame)
        bio_label.grid(row = 0, column = 2)
        self.bio_input.grid(row = 1, column= 2)
    #create gender label , inputs and render it
        gender = tkinter.Label(personal_info_frame, text="Gender")
        self.gender_combobox = ttk.Combobox(personal_info_frame, values=["Male", "Female", "rather not say"])
        self.gender_combobox.set("Select an option")
        gender.grid(row= 2, column= 0 )
        self.gender_combobox.grid(row=3, column= 0)
    #create age_label, input and render it
        age_label = tkinter.Label(personal_info_frame, text="Age")
        self.age_spinbox = tkinter.Spinbox(personal_info_frame, from_=13 , to= 90 )
        age_label.grid(row=2 , column=1)
        self.age_spinbox.grid(row=3, column=1)
    #create nationality label, input fetching and render it
        nationality_label = tkinter.Label(personal_info_frame, text="Nationality")
        self.nationality_input = ttk.Combobox(personal_info_frame, values = self.countries_data)
        self.nationality_input.set("Select an option")
        nationality_label.grid(row=2, column=2)
        self.nationality_input.grid(row= 3, column= 2)

    #set padding for personal inputs
        for widget in personal_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady= 5)

        ##################################################
        #           start by account info                #
        ##################################################

        account_info_frame = tkinter.LabelFrame(self.add_user_frame, text= "Account_Information")
        account_info_frame.grid(row=1 , column= 0,sticky="news",padx=10, pady=10)
    #create email label , inputs and render it
        email_label = tkinter.Label(account_info_frame, text="Email")
        self.email_input = tkinter.Entry(account_info_frame)
        email_label.grid(row = 2, column = 1)
        self.email_input.grid(row = 3, column= 1)
    #create password_label , inputs and render it
        password_label = tkinter.Label(account_info_frame, text="Password")
        self.password_input = tkinter.Entry(account_info_frame , show="*")
        password_label.grid(row = 2, column = 2)
        self.password_input.grid(row = 3, column= 2)
    #create show_password_btn_label , inputs and render it
        self.show_password_toggle = tkinter.BooleanVar()
        show_password_btn_label = tkinter.Checkbutton(account_info_frame, text="show Password",variable=self.show_password_toggle, command=self.togglePassword)
        show_password_btn_label.grid(row = 3, column = 4)

    #set padding for personal inputs
        for widget in account_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady= 5)

        ##################################################
        #           start by terms & conditions info     #
        ##################################################

        terms_conditions_frame = tkinter.LabelFrame(self.add_user_frame, text= "Terms & Conditions")
        terms_conditions_frame.grid(row=2 , column= 0,sticky="news",padx=10, pady=10)
    #create terms_btn_label , inputs and render it
        self.term_var = tkinter.StringVar(value=False)
        terms_btn_label = tkinter.Checkbutton(terms_conditions_frame, text="Accept all terms and conditions", variable=self.term_var, onvalue=True,offvalue=False)
        terms_btn_label.grid(row = 0, column = 0)        

        ##################################################
        #                 start by buttons               #
        ##################################################
        save_btn = tkinter.Button(self.add_user_frame, text="Save" ,bg="green",fg="white", command= self.handleForm, cursor="hand2")
        account_btn = tkinter.Button(self.add_user_frame, text="Go to my account"  ,bg="blue",fg="white",command=self.switch_to_login_page, cursor="hand2")
        exit_btn = tkinter.Button(self.add_user_frame, text="Exit"  ,bg="red",fg="white",command=self.exitProgram, cursor="hand2")
        save_btn.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        exit_btn.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        account_btn.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.root.mainloop()
        ##################################################
        #                 Error handling                 #
        ##################################################

    def handleForm(self):
        fullname = self.fullname_input.get()
        age = self.age_spinbox.get()
        gender = self.gender_combobox.get()
        email = self.email_input.get()
        password = self.password_input.get()
        nationality =self. nationality_input.get()
        hobbies = self.hobbies_input.get()
        acceptedTerms = self.term_var.get()
        bio = self.bio_input.get()
        if not fullname:
             tkinter.messagebox.showerror(title="fullname Error" , message="Full name Field required")
        elif not re.match("^(?=.{3,}$)[a-zA-Z]+( [a-zA-Z]+)?$", fullname):
               tkinter.messagebox.showerror(title="fullname Error" , message="fullname not acceptable . it should not contain any spetial characteres (/*@#$) or numbers(0--->9) and should contain at least 3 characteres")
        elif gender not in ["Male", "Female", "rather not say"]:
              tkinter.messagebox.showerror(title="Gender Error", message="Gender should be one from the list")
        elif nationality not in self.countries_data:
              tkinter.messagebox.showerror(title="Nationality Error", message="Nationality should be one from the list")
        elif not email :
             tkinter.messagebox.showerror(title="Email Error" , message="Email Field required")
        elif not re.match("^[a-zA-Z_]{3,}[0-9]@(?:gmail\\.com|hotmail\\.com)$", email):
            tkinter.messagebox.showerror(title="Email Error", message="Email should be as format : Example1@gmail/hotmail.com")
        elif not password :
             tkinter.messagebox.showerror(title="Password Error" , message="Password Field required")
        elif not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*])[A-Za-z\\d!@#$%^&*]{8,}$", password):
            tkinter.messagebox.showerror(title="Password Error", message="strong password should contain Minimum 8 characters. At least one uppercase letter. At least one lowercase letter. At least one number. At least one special character (e.g., !@#$%^&*).")
        else :
            if acceptedTerms == '1':
                data = {
                "fullname" : fullname,
                "age" : age,
                "gender" : gender,
                "email" : email,
                "password" : password,
                "nationality" : nationality,
                "hobbies" : hobbies or None,
                "bio" : bio or None,
                "term_policy":acceptedTerms,
                "friend_count" : 0,
                "friend_list" : {},
                "isActive" : False,
                }
                self.setUserData(data)
                self.clearForm()
            else:
                tkinter.messagebox.showwarning(title="fullname Error", message="terms & policy should be accepted")

        ##################################################
        #                 set User Data                  #
        ##################################################

    def setUserData(self, data):

        result = self.friend.register(data)
        if not result :
            tkinter.messagebox.showerror(title="Email Exist" , message="Email is already in use...please try another one or log in")
        else :
            tkinter.messagebox.showinfo(title="Adding user successfuly", message=f"{data['email']} have been added successfuly :)")


        ##################################################
        #            Reste form after submit it          #
        ##################################################

    def clearForm(self):
        self.fullname_input.delete(0 , "end")
        self.hobbies_input.delete(0, "end")
        self.bio_input.delete(0, "end")
        self.age_spinbox.delete(0, 'end')
        self.age_spinbox.insert(0, 13)
        self.gender_combobox.set("Select an option")
        self.nationality_input.set("Select an option")
        self.email_input.delete(0, "end")
        self.password_input.delete(0, "end")
        self.term_var.set(False)

        ##################################################
        #               toggle the password              #
        ##################################################

    def togglePassword(self):
            if self.show_password_toggle.get():
                self.password_input.config(show="")
            else:
                self.password_input.config(show="*") 

        ##################################################
        #            Exit button functionality           #
        ##################################################

    def exitProgram(self):
            self.root.destroy()

        ##################################################
        #                 switch to login                #
        ##################################################
                 
    def switch_to_login_page(self):
            self.add_user_frame.destroy()
            self.loginPage()
        ##################################################
        #                  login page                    #
        ##################################################

    def loginPage(self):
        self.login_frame = tkinter.Frame(self.root)
        self.login_frame.configure(bg="#eeeeee")
        #to save my frame
        self.login_frame.grid(row=0, column=0, padx=500, pady=400)
        # Email Label and Entry
        email_label = tkinter.Label(self.login_frame, text="Email:")
        email_label.grid(row=0,column=0)
        self.email_login = tkinter.Entry(self.login_frame, width=40)
        self.email_login.grid(row=0,column=1)

        # Password Label and Entry
        password_label = tkinter.Label(self.login_frame, text="Password:")
        password_label.grid(row=1,column=0,pady=10)
        self.password_login = tkinter.Entry(self.login_frame, width=40) 
        self.password_login.grid(row=1,column=1,pady=5)
        
        # Button to submit
        submit_button = tkinter.Button(self.login_frame, text="Log in" ,bg="green",fg="white", width=5, command=self.handleLoginPage, cursor="hand2")
        submit_button.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        ##################################################
        #                  handleLoginPage fct           #
        ##################################################

    def handleLoginPage(self):
        email = self.email_login.get()
        password = self.password_login.get()
        if not email :
             tkinter.messagebox.showerror(title="Email Error" , message="Email Field required")
        elif not re.match("^[a-zA-Z_]{3,}[0-9]@(?:gmail\\.com|hotmail\\.com)$", email):
            tkinter.messagebox.showerror(title="Email Error", message="Email should be as format : Example1@gmail/hotmail.com")
        else:
            result =  self.friend.login(email, password)
            if not result:
                tkinter.messagebox.showerror(title="Login Error", message="Email or password incorrect")
            else:
                tkinter.messagebox.showinfo(title="Login successfull", message="Login successful :)")
                self.switch_to_profile(result)
        ##################################################
        #                 switch to Profile              #
        ##################################################
                 
    def switch_to_profile(self, user):
            self.login_frame.destroy()
            self.profilePage(user)

        ##################################################
        #                  Profile page                  #
        ##################################################

    def profilePage(self, current_user):
        for widget in self.root.winfo_children():
            widget.destroy()
        profile_page_frame = tkinter.Frame(self.root, padx=20, pady= 100)
        profile_page_frame.grid(row = 0, column= 0 , padx=500, pady=50)
        profile_page_frame.configure(bg="#eeeeee")
        row = 1
        header_label = ttk.Label(profile_page_frame, text=f"Welcome Back {current_user['fullname']}", font=("Abocat", 30, "bold"))
        header_label.grid(row=0, column=0, sticky="w", pady=5)
        for key, value in current_user.items():

            # Create label for key
            if key == 'term_policy' or key == 'friend_list':
                continue
            key_label = ttk.Label(profile_page_frame, text=f"{key.capitalize()}: ", font=("Arial", 12, "bold"))
            key_label.grid(row=row, column=0, sticky="w", pady=5)

            # Create label for value
            value_label = ttk.Label(profile_page_frame, text=f"{value}", font=("Arial", 12), wraplength=200, justify="left")
            value_label.grid(row=row, column=1, sticky="w", pady=5)
            row +=1
        
        #add list friend manually to avoid overflow
            key_label = ttk.Label(profile_page_frame, text=f"{"friend_list".capitalize()}: ", font=("Arial", 12, "bold"))
            key_label.grid(row=11, column=0, sticky="w", pady=5)

            value_label = ttk.Label(profile_page_frame, text=f"{list(current_user['friend_list'])[0] if current_user['friend_list'] else "No friends..."}", font=("Arial", 12))
            value_label.grid(row=11, column=1, sticky="w", pady=5)
            
        #so only if there are more than one friend
        # i used get because ['2'] give me an error 
            if current_user['friend_count'] > 0:

        #see more from the list 
                anchor = tkinter.Label(profile_page_frame, text="See more...", font=("Arial", 12), fg="blue", cursor="hand2")
                anchor.grid(row=12, column=1, sticky="w", pady=5)
            
        #add functionality for see more
                anchor.bind("<Button-1>", lambda e: self.swich_to_friendList_user( current_user, profile_page_frame))

            

        #lambda is like ()=> ananymus function in js so now i can pass parameter for the follow page
        Follow_btn = tkinter.Button(profile_page_frame, text="Let's find some Friends" ,bg="grey",fg="white", command=lambda : self.handleFollow(current_user, profile_page_frame) , cursor="hand2")
        Follow_btn.grid(row=row + 3, column=0, padx=10, pady=5, sticky="ew")
        logout_btn = tkinter.Button(profile_page_frame, text="Log out"  ,bg="red",fg="white", command=lambda :self.handleLogout(current_user, profile_page_frame), cursor="hand2")
        logout_btn.grid(row=row + 2, column=0, padx=10, pady=5, sticky="ew",)
        
        ##################################################
        #             switch to friend list              #
        ##################################################
                 
    def swich_to_friendList_user(self, current_user, parent_frame):
            parent_frame.destroy()
            self.seeMoreFriend( current_user)
    
        ##################################################
        #             handle see more friend             #
        ##################################################
        
    def seeMoreFriend(self, current_user):
    #this code because i face an conflict when i destroy frames and switch between pages
    #so it check when i render this component that all frames are destoyed normaly
        for widget in self.root.winfo_children():
            widget.destroy()
        #fetching data 
        with open('userDB.json', 'r') as file :
            users_data = json.load(file)
        
        friends_frame = tkinter.Frame(self.root)
        friends_frame.grid(row=0, column=0, padx=220)

        #create header
        # header_label = ttk.Label(friends_frame, text=f"This you friends list {current_user['fullname']}", font=("Abocat", 30, "bold"))
        # header_label.grid(row=0, column=1, sticky="w", pady=50, padx= 150)

        friend_labelframe = tkinter.LabelFrame(friends_frame, bg="#f5f5f5", text=f"{current_user['fullname'].capitalize()}'s friend list")
        friend_labelframe.grid_propagate(False)
        friend_labelframe.grid(row=1, column=1, sticky="w")

        canvas = tkinter.Canvas(friend_labelframe, bg="#f5f5f5", width=1040, height=800)
        canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.TRUE)

        scrollbar = tkinter.Scrollbar(friend_labelframe, orient=tkinter.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        scrollable_frame = tkinter.Frame(canvas, bg="#f5f5f5", pady=30)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")


        row = 0
        col = 0

        for friend_key, friend_value in current_user['friend_list'].items():
            if col % 2 == 0:
                row += 1
                col = 0

            # Create a LabelFrame for each friend
            friend_label_frame = tkinter.LabelFrame(scrollable_frame, bg="#f5f5f5", text=f"{users_data[friend_value]['fullname'].capitalize()}", padx=50, pady=10, width=500, height=500)
            friend_label_frame.grid_propagate(False)

            inner_row = 0
            for key, value in users_data[friend_value].items():
                if key == "term_policy" or key == "password":
                    continue
                
                # Create a label for the key (in bold)
                key_label = tkinter.Label(friend_label_frame, text=key.capitalize(), font=("Arial", 12, "bold"), bg="#f5f5f5", wraplength=400, justify="left")
                key_label.grid(row=inner_row, column=0, sticky="w", pady=5)

                # Create a label for the value
                value_label = tkinter.Label(friend_label_frame, text=value, font=("Arial", 12), bg="#f5f5f5", wraplength=400, justify="left")
                value_label.grid(row=inner_row, column=1, sticky="w", pady=5)

                inner_row += 1

            # Create the unfollow button at the bottom of each LabelFrame
            unfollow_btn = tkinter.Button(friend_label_frame, text="Unfollow", bg="red", fg="white",command=lambda destinationUser = users_data[friend_value]: self.triggerUnfollow(current_user, destinationUser['email']), cursor="hand2")
            unfollow_btn.grid(row=inner_row, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

            friend_label_frame.grid(row=row, column=col, sticky="w", pady=10, padx=10)

            col += 1

        #create back btn
        refresh_btn = tkinter.Button(scrollable_frame, text="Back", bg='blue', fg="white", pady=0, command= lambda  : self.switchBackToProfilePage(current_user, friends_frame), cursor="hand2")
        refresh_btn.grid(row=row + 2, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        ##################################################
        #                  trigger unfollow              #
        ##################################################

    def triggerUnfollow (self, current_user, destinationUser_email):
        result = self.friend.unfollow(current_user, destinationUser_email)
        if result:
            tkinter.messagebox.showinfo(title="unfollow result", message=f"you dumped {destinationUser_email} good for you ;)")
        #re render the component with the new data
            self.seeMoreFriend(result)
        else :
            tkinter.messagebox.showinfo(title="unfollow result", message=f"You're Lonely . You don't even have a friends to remove it :(")
            
        ##################################################
        #                  handleBackfct                 #
        ##################################################

    def switchBackToProfilePage(self, current_user, parent_frame):
        parent_frame.destroy()
        self.profilePage(current_user)

        ##################################################
        #                  handle logout                 #
        ##################################################
        
    def handleLogout(self, current_user, parent_frame):
        current_user['isActive'] = False
        parent_frame.destroy()
        self.addUser()

        ##################################################
        #                  handle FollowPage              #
        ##################################################
        
    def handleFollow(self, user, parent_frame):
        parent_frame.destroy()
        self.followPage(user)

    def createHeader(self, current_user):
        header_label = ttk.Label(self.root, text=f"Let's have some Friends {current_user['fullname']}", font=("Abocat", 30, "bold"))
        header_label.grid(row=1, column=0, sticky="w", pady=50, padx=500)

        ##################################################
        #              createFollowPageFrame             #
        ##################################################

    def createFollowPageFrame(self):
    #user is the data for user which i log in by so i won't see in my users list because i can't follow it
        self.follow_page_frame = tkinter.Frame(self.root, padx=250, pady= 0, width=800)
        self.follow_page_frame.grid(row=3, column=0, sticky="w", pady=5, padx=5, ipadx=5, ipady=5)
        self.follow_page_frame.configure(bg="#eeeeee")

        ##################################################
        #                  follow Page                   #
        ##################################################

    def followPage(self, current_user, filtred_users= None):
    #so when filtred_users = None it means filter.value == reset so i reset the whole form
        users = None
        if filtred_users :
            users = filtred_users
        else :
        #then the user enter reset or dont find a similiarity
        #get all data from data base
            with open('userDB.json','r') as file:
                users = json.load(file)
    #nested component in my window
        self.root.configure(bg="#ececec", width=880)

    #create header for page
        self.createHeader(current_user)

    #create follow page frame
        self.createFollowPageFrame()


    #create canvas for scrolling 
        my_canvas = tkinter.Canvas(self.follow_page_frame, width=1200, height=600)
        my_canvas.grid(row=4, column=0, sticky="nsew", columnspan=2)

        #add scroll bar
        my_scrollbar = tkinter.Scrollbar(self.follow_page_frame , orient="vertical", command=my_canvas.yview)
        my_scrollbar.grid(row=4, column=2, sticky="ns")

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        
        second_frame = tkinter.Frame(my_canvas)
        my_canvas.create_window((0 , 0), window = second_frame, anchor = 'nw')

    #create like filter to filter by some data
        filter_value = ['hobbies', 'fullname', 'nationality', 'reset']
        self.filter_input = ttk.Combobox(self.follow_page_frame, values =filter_value)
    #to add the functionality
        self.filter_input.bind("<<ComboboxSelected>>",lambda e: self.handleFilter(current_user, self.filter_input.get()))

        self.filter_input.set("Filter By")
        self.filter_input.grid(row= 0, column= 1)

        row, col = 0, 0
        max_cols = 3 
        
        for email, user_data in users.items():
            if col % max_cols == 0:
                row += 1
                col = 0
            
            if email == current_user['email']:
                continue
            
            user_frame = tkinter.LabelFrame(second_frame, bg="#f5f5f5", text=email, padx=50, pady=10, highlightbackground='red', highlightthickness=2)
            user_frame.grid(row=row, column=col, padx=10, pady=10, sticky="w")
            
            max_label_length = 0
            
            for user_key, user_value in user_data.items():

    #skip these data because it not make since to display password
                if user_key in ['term_policy', 'password', 'email']:
                    continue

    #stop display other data 
                if user_data['isActive'] == True:
                    break
                label = tkinter.Label(user_frame, text=f"{user_key}: {user_value}", font=("Arial", 12), bg="#f5f5f5", wraplength=200, justify="left")
                label.grid(sticky="w", pady=5)
                
                label_length = len(f"{user_key}: {user_value}")
                if label_length > max_label_length:
                    max_label_length = label_length
            
            follow_btn = tkinter.Button(user_frame, text="Follow", bg="blue", fg="white", command=lambda user = user_data: self.trigger_follow(current_user, user), cursor="hand2")
            follow_btn.grid(padx=10, pady=5, sticky="ew")
            
            user_frame.grid_propagate(False)
            user_frame.config(width=300, height=400 + (max_label_length * 2))
            
            col += 1
        back_btn = tkinter.Button(second_frame, text="Back", bg="silver", fg="black", command=lambda : self.backToProfile(current_user), cursor="hand2")
        back_btn.grid(row=5, column= 1, sticky='news', pady=20)
        my_canvas.update_idletasks() 
        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
        my_canvas.configure(scrollregion=my_canvas.bbox("all"))
        self.root.mainloop()

        ##################################################
        #                  backToProfile                 #
        ##################################################

    def backToProfile(self, current_user):
        self.follow_page_frame.destroy()
        self.profilePage(current_user)


        ##################################################
        #                  handleFilter                  #
        ##################################################

    def handleFilter(self, current_user, searching_by):
        if searching_by == 'reset':
            self.followPage(current_user, self.user_data)
        
        #that's mean values for current_user with this seaching_by == None or empty so we cann't filter bysomething i did'nt even have it
        if not current_user[searching_by]:
           return tkinter.messagebox.showwarning(title="Filter result" , message=f"You didn't even have {searching_by} data")

        result = self.friend.dfsSearch(current_user['email'], searching_by, current_user[searching_by])
        if result :
            self.followPage(current_user, result)
        else:
            tkinter.messagebox.showinfo(title="Filter result" , message=f"No one share with you the same {searching_by}...because you're AWESOME!!!")

        ##################################################
        #                  FOllow function               #
        ##################################################

    def trigger_follow(self, current_user_email, user_to_follow_email):
        
        result = self.friend.follow(current_user_email, user_to_follow_email)
        
        tkinter.messagebox.showinfo(title="Follow Result", message=result)
        self.friend.displayFriendList()




def main():
    app = NewUser()
    # app .addUser()
    app.followPage( {
    "fullname": "aboud",
    "age": "13",
    "gender": "Male",
    "email": "aboud1@gmail.com",
    "password": "Aboud123!",
    "nationality": "Afghanistan",
    "hobbies": None,
    "bio": None,
    "term_policy": "1",
    "friend_list": {
      "aboud4@gmail.com": "aboud4@gmail.com",
      "aboud5@gmail.com": "aboud5@gmail.com",
      "aboud2@gmail.com": "aboud2@gmail.com",
      "aboud3@gmail.com": "aboud3@gmail.com",
      "aboud6@gmail.com": "aboud6@gmail.com",
      "aboud7@gmail.com": "aboud7@gmail.com",
    },
    "isActive": False,
    "friend_count": 6
  })
main()