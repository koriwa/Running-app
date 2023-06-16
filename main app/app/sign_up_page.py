import tkinter as tk
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

sign_up_page = customtkinter.CTk()
sign_up_page.geometry("495x595")
sign_up_page.resizable(width=False, height=False)
sign_up_page.title('Sign Up')
accounts_file = "G:/My Drive/main app/app/db/accounts.txt"


def button_function():
    # Get the entered values from the input fields
    username = User_name_box.get()
    password = Password_box.get()
    confirm_password = confirm_password_box.get()

    # Check if the password matches the confirm password
    if password == confirm_password:
        # Open the accounts file in read and write mode
        with open(accounts_file, "r+") as file:
            # Read all the lines from the file
            lines = file.readlines()

            # checks each line for the user so it knows stuff
            for line in lines:
                # Check if the combination of username and password already exists in the file 
                if (username + ":" + password + "\n") in line:
                    # prints a msgs if the user exists
                    print("User already exists, please create a different account")
                    break
            else:
                # If the combination doesn't exist, it writes the new username and password to the file and saves it 
                file.write(username + ":" + password + "\n")
                # Destroy the sign-up page
                sign_up_page.destroy()
                # Imports the log in page so you can enter your credintials again
                import log_in_page
    else:
        # Print a message if the password doesn't match with the confirm password
        print("Passwords do not match")



background = "app/assets/cat.png"
background_image = ImageTk.PhotoImage(Image.open(background))
kat_label = customtkinter.CTkLabel(master=sign_up_page, image=background_image)
kat_label.pack()

frame = customtkinter.CTkFrame(
    master=kat_label, width=320, height=400, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

login_label = customtkinter.CTkLabel(
    master=frame, text="Sign Up", font=('Century Gothic', 30))
login_label.place(x=110, y=45)

User_name_box = customtkinter.CTkEntry(
    master=frame, width=220, placeholder_text='Username')
User_name_box.place(x=50, y=110)

Password_box = customtkinter.CTkEntry(
    master=frame, width=220, placeholder_text='Password', show='*')
Password_box.place(x=50, y=165)

confirm_password_box = customtkinter.CTkEntry(
    master=frame, width=220, placeholder_text='Confirm Password', show='*')
confirm_password_box.place(x=50, y=220)

sign_in_button = customtkinter.CTkButton(
    master=frame, width=220, text="Sign Up", command=button_function, corner_radius=6)
sign_in_button.place(x=50, y=275)

sign_up_page.mainloop()
