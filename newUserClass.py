import tkinter
import re 
import requests
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox 
import json
class newUSer:
    def __init__(self) -> None:
        self.fullname_input = ""
        self.hobbies_input= ""
        self.bio_input = ""
        self.age_spinbox = ""
        self.gender_combobox = ""
        self.nationality_input = ""
        self.email_input = ""
        self.password_input = ""
        self.term_var = False
        self.following = 0
        self.followers = 0
        self.isActive = False
    #initial following_list and followers_list by dictionary to avoid duplicate
        self.following_list = {}
        self.followers_list = {}
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
        self.profile_page_frame = tkinter.Frame(self.root, padx=20, pady= 20)
        

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
        self.add_user_frame.pack(padx=100, pady=100)
        
        ##################################################
        #           start by Personal info               #
        ##################################################

    #saving personal info
        personal_info_frame = tkinter.LabelFrame(self.add_user_frame, text= "Personal_Information")
        personal_info_frame.grid(row=0 , column= 0 ,padx=10, pady=10)

    #create full_name label , inputs and render it
        full_name_label = tkinter.Label(personal_info_frame, text="Full name")
        self.full_name_input = tkinter.Entry(personal_info_frame)
        full_name_label.grid(row = 0, column = 0)
        self.full_name_input.grid(row = 1, column= 0)
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
        save_btn = tkinter.Button(self.add_user_frame, text="Save" ,bg="green",fg="white", command= self.handleForm)
        account_btn = tkinter.Button(self.add_user_frame, text="Go to my account"  ,bg="blue",fg="white",command=self.switch_to_login_page)
        exit_btn = tkinter.Button(self.add_user_frame, text="Exit"  ,bg="red",fg="white",command=self.exitProgram)
        save_btn.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        exit_btn.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        account_btn.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.root.mainloop()
        ##################################################
        #                 Error handling                 #
        ##################################################

    def handleForm(self):
        fullname = self.full_name_input.get()
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
                "hobbies" : hobbies,
                "bio" : bio,
                "term_policie":acceptedTerms,
                "following" : 0,
                "followers" : 0,
                "isActive" : 0,
                "following_list" : {},
                "followers_list" : {},
                }
                self.setUserData(data)
                self.clearForm()
            else:
                tkinter.messagebox.showwarning(title="fullname Error", message="terms & policy should be accepted")

        ##################################################
        #                 set User Data                  #
        ##################################################

    def setUserData(self, data):
    #check if data already exist in my self.user_data dictionary
    #so self.user_data dictionary here is like small DB 
        self.user_data[data['email']] = data
        with open("userDB.json", 'r') as file:
            existing_data = json.load(file)
        if data['email'] in existing_data:
            tkinter.messagebox.showerror(title="Email Exist" , message="Email is already in use...please try another one or log in")
        else :
            existing_data[data['email']] = data
            with open("userDB.json", 'w') as file:
                json.dump(existing_data, file)


        ##################################################
        #            Reste form after submit it          #
        ##################################################

    def clearForm(self):
        self.full_name_input.delete(0 , "end")
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
        self.login_frame = tkinter.Frame(self.root, padx=20, pady= 20)
        self.login_frame.configure(bg="#eeeeee")
        #to save my frame
        self.login_frame.pack(padx=100, pady=100)
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
        submit_button = tkinter.Button(self.login_frame, text="Log in" ,bg="green",fg="white", width=5, command=self.handleLoginPage)
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
            with open('userDB.json', 'r') as file:
                users = json.load(file)
                if email in users:
                    if password == users[email]['password']:
                #set is active true
                        users[email]['isActive'] = True
                        self.switch_to_profile(users[email])
                    else:
                        tkinter.messagebox.showerror(title="Login Error", message="Email or password incorrect")
                else:
                    tkinter.messagebox.showerror(title="Login Error", message="Email or password incorrect")
    
        ##################################################
        #                 switch to Profile              #
        ##################################################
                 
    def switch_to_profile(self, user_email):
            self.login_frame.destroy()
            self.profilePage(user_email)

        ##################################################
        #                  Profile page                  #
        ##################################################

    def profilePage(self, user):
        self.profile_page_frame = tkinter.Frame(self.root, padx=20, pady= 20)
        self.profile_page_frame.pack(padx=300, pady=100)
        self.profile_page_frame.configure(bg="#eeeeee")
        row = 1
        header_label = ttk.Label(self.profile_page_frame, text=f"Welcome Back {user['fullname']}", font=("Abocat", 30, "bold"))
        header_label.grid(row=0, column=0, sticky="w", pady=5)
        for key, value in user.items():
            # Create label for key
            key_label = ttk.Label(self.profile_page_frame, text=f"{key.capitalize()}: ", font=("Arial", 12, "bold"))
            key_label.grid(row=row, column=0, sticky="w", pady=5)

            # Create label for value
            value_label = ttk.Label(self.profile_page_frame, text=f"{value}", font=("Arial", 12))
            value_label.grid(row=row, column=1, sticky="w", pady=5)
            row +=1
        Follow_btn = tkinter.Button(self.profile_page_frame, text="Let's find some Friends" ,bg="grey",fg="white", command=self.handleFollow)
        Follow_btn.grid(row=row + 2, column=0, padx=10, pady=5, sticky="ew")
        logout_btn = tkinter.Button(self.profile_page_frame, text="Log out"  ,bg="red",fg="white", command=self.handleLogout)
        logout_btn.grid(row=row + 1, column=0, padx=10, pady=5, sticky="ew",)

        ##################################################
        #                  handle logout                 #
        ##################################################
        
    def handleLogout(self):
        self.profile_page_frame.destroy()
        self.addUser()

        ##################################################
        #                  handle Follow                 #
        ##################################################
        
    def handleFollow(self):
        self.profile_page_frame.destroy()
        self.usersPage()

        ##################################################
        #                  users Page                    #
        ##################################################
    def usersPage(self):
        self.follow_page_frame = tkinter.Frame(self.root, padx=20, pady= 20)
        self.follow_page_frame.pack(padx=300, pady=100)
        self.follow_page_frame.configure(bg="#eeeeee")
    #get data from data base
        with open('userDB.json','r') as file:
            users = json.load(file)
        row = 0
        for key, value in users.items():
            fullname = ttk.Label(self.follow_page_frame, text=f"Full name : {value['fullname']}",font=("Arial", 12))
            fullname.grid(row=row, column=0, sticky="w", pady=5)
            row += 1
            email = ttk.Label(self.follow_page_frame, text=f"Email : {key}", font=("Arial", 12))
            email.grid(row=row, column=0, sticky="w", pady=5)
            row +=1