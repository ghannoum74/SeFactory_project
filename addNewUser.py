import tkinter
import re
import requests
import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
##################################################
#                 Error handling                 #
##################################################

def handleForm(full_name_input, age_spinbox, gender_combobox, email_input, password_input, nationality_input, hobits_input, bio_input, term_var, countries_data):
        fullname = full_name_input.get()
        age = age_spinbox.get()
        gender = gender_combobox.get()
        email = email_input.get()
        password = password_input.get()
        nationality = nationality_input.get()
        hobits = hobits_input.get()
        acceptedTerms = term_var.get()
        bio = bio_input.get()
        if not fullname:
             tkinter.messagebox.showerror(title="fullname Error" , message="Full name Field required")
        elif not re.match("^(?=.{3,}$)[a-zA-Z]+( [a-zA-Z]+)?$", fullname):
               tkinter.messagebox.showerror(title="fullname Error" , message="fullname not acceptable . it should not contain any spetial characteres (/*@#$) or numbers(0--->9) and should contain at least 3 characteres")
        elif gender not in ["Male", "Female", "rather not say"]:
              tkinter.messagebox.showerror(title="Gender Error", message="Gender should be one from the list")
        elif nationality not in countries_data:
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
                friend_data = {
                "fullname" : fullname,
                "age" : age,
                "gender" : gender,
                "email" : email,
                "password" : password,
                "nationality" : nationality,
                "hobits" : hobits,
                "bio" : bio,
                "term & policie":acceptedTerms
                }
                print (friend_data)
                clearForm()
            else:
                tkinter.messagebox.showwarning(title="fullname Error", message="terms & policy should be accepted")

def clearForm():
     pass
def addUser():
        #TOGGLE PASSWORD FORM 
        def togglePassword():
            if show_password_tggle.get():
                password_input.config(show="")
            else:
                password_input.config(show="*")
#parent component
        window = tkinter.Tk()
#title for my GUI program
        window.title("Friendship Community")
#nested component in my window
        frame = tkinter.Frame(window, padx=20, pady= 20)
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
        gender_combobox.set("Select an option")
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
        countries_data =[county["name"] for county in req.json()[:150]]
        nationality_input = ttk.Combobox(personal_info_frame, values = countries_data)
        nationality_input.set("Select an option")
        nationality_label.grid(row=2, column=2)
        nationality_input.grid(row= 3, column= 2)

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
        email_input = tkinter.Entry(account_info_frame)
        email_label.grid(row = 2, column = 1)
        email_input.grid(row = 3, column= 1)
#create password_label , inputs and render it
        password_label = tkinter.Label(account_info_frame, text="Password")
        password_input = tkinter.Entry(account_info_frame , show="*")
        password_label.grid(row = 2, column = 2)
        password_input.grid(row = 3, column= 2)
#create show_password_btn_label , inputs and render it
        show_password_tggle = tkinter.BooleanVar()
        show_password_btn_label = tkinter.Checkbutton(account_info_frame, text="show Password",variable=show_password_tggle, command=togglePassword)
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
        term_var = tkinter.StringVar(value=False)
        terms_btn_label = tkinter.Checkbutton(terms_conditions_frame, text="Accept all terms and conditions", variable=term_var, onvalue=True,offvalue=False)
        terms_btn_label.grid(row = 0, column = 0)        

        ##################################################
        #                 start by button                #
        ##################################################
        def errorHandlingFct():
                 handleForm(full_name_input,
                           age_spinbox,
                           gender_combobox,
                           email_input,
                           password_input,
                           nationality_input,
                           hobits_input,
                           bio_input,
                           term_var,
                           countries_data)
        button = tkinter.Button(frame, text="Submit" , command= errorHandlingFct)
        button.grid(row = 3, column=0, sticky="news",padx=10, pady=10)
        print()


#to run my window component
        window.mainloop()