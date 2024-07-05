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

        ##################################################
        #                 get User Data                  #
        ##################################################

    # def getUserData(self):
    #      return self.user_data
    
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
        #                 Go to my account               #
        ##################################################

    def myAccount(self):
        new_window = tkinter.Toplevel(self.root)
        new_window.title("New Window")
        new_window.geometry("700x200")

        # Email Label and Entry
        email_label = tkinter.Label(new_window, text="Email:")
        email_label.pack(pady=5)
        email_entry = tkinter.Entry(new_window, width=40)
        email_entry.pack(pady=5)

        # Password Label and Entry
        password_label = tkinter.Label(new_window, text="Password:")
        password_label.pack(pady=10)
        password_entry = tkinter.Entry(new_window, show="*", width=40)  # show="*" to mask the password
        password_entry.pack(pady=5)
        

        # Button to submit
        submit_button = tkinter.Button(new_window, text="Submit")
        submit_button.pack(pady=10)

        ##################################################
        #                 create new user                #
        ##################################################
         
    def addUser(self):
    #title for my GUI program
        self.root.title("Friendship Community")
    #nested component in my window
        frame = tkinter.Frame(self.root, padx=20, pady= 20)
        #to save my frame
        frame.pack(padx=100, pady=100)

        ##################################################
        #           start by Personal info               #
        ##################################################

    #saving personal info
        personal_info_frame = tkinter.LabelFrame(frame, text= "Personal_Information")
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

        account_info_frame = tkinter.LabelFrame(frame, text= "Account_Information")
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

        terms_conditions_frame = tkinter.LabelFrame(frame, text= "Terms & Conditions")
        terms_conditions_frame.grid(row=2 , column= 0,sticky="news",padx=10, pady=10)
    #create terms_btn_label , inputs and render it
        self.term_var = tkinter.StringVar(value=False)
        terms_btn_label = tkinter.Checkbutton(terms_conditions_frame, text="Accept all terms and conditions", variable=self.term_var, onvalue=True,offvalue=False)
        terms_btn_label.grid(row = 0, column = 0)        

        ##################################################
        #                 start by buttons               #
        ##################################################
        save_btn = tkinter.Button(frame, text="Save" ,bg="green",fg="white", command= self.handleForm)
        account_btn = tkinter.Button(frame, text="Go to my account"  ,bg="blue",fg="white",command=self.myAccount)
        exit_btn = tkinter.Button(frame, text="Exit"  ,bg="red",fg="white",command=self.exitProgram)
        save_btn.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        exit_btn.grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        account_btn.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.root.mainloop()

    
