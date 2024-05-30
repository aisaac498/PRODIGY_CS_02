import customtkinter as ctk
from tkinter import StringVar
import re
from PIL import Image, ImageTk

# 1st Modification: Allow the user to toggle between light and dark mode and change the button icon
def toggle_mode():
    if ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("Dark")
        mode_button.configure(image=sun_image, text="")
    else:
        ctk.set_appearance_mode("Light")
        mode_button.configure(image=moon_image, text="")

def check_password_strength():
    password = password_var.get()
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search("[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search("[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    display_feedback(strength, feedback)

def display_feedback(strength, feedback):
    if strength == 5:
        feedback_label.configure(text="Password is very strong!", text_color="green")
    elif strength >= 3:
        feedback_label.configure(text="Password is moderate. " + " ".join(feedback), text_color="orange")
    else:
        feedback_label.configure(text="Password is weak. " + " ".join(feedback), text_color="red")

# 2nd Modification: Make the feedback label text wrap based on the window size
def wrap_feedback(event):
    feedback_label.configure(wraplength=app.winfo_width() - 40)

# 3rd Modification: Allow the user to reveal the written password
def toggle_password_visibility():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        toggle_visibility_button.configure(text="Hide Password")
    else:
        password_entry.configure(show="*")
        toggle_visibility_button.configure(text="Show Password")

app = ctk.CTk()
app.title("Password Strength Checker")
app.geometry("400x300")

password_var = StringVar()
password_entry = ctk.CTkEntry(app, textvariable=password_var, width=300, show="*")
password_entry.pack(pady=20)

# 4th Modification: Center the buttons in the middle of the screen
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

check_button = ctk.CTkButton(button_frame, text="Check Password Strength", command=check_password_strength)
check_button.pack(pady=5)

toggle_visibility_button = ctk.CTkButton(button_frame, text="Show Password", command=toggle_password_visibility)
toggle_visibility_button.pack(pady=5)

feedback_label = ctk.CTkLabel(app, text="", wraplength=360)
feedback_label.pack(pady=10)

# Load and resize images
sun_image_path = "images/sun.png"  # Replace with the path to your sun image
moon_image_path = "images/moon.png"  # Replace with the path to your moon image

sun_image_pil = Image.open(sun_image_path).resize((32, 32), Image.Resampling.LANCZOS)
moon_image_pil = Image.open(moon_image_path).resize((32, 32), Image.Resampling.LANCZOS)

# Convert Image objects to PhotoImage objects using ImageTk
sun_image = ImageTk.PhotoImage(sun_image_pil)
moon_image = ImageTk.PhotoImage(moon_image_pil)

# Position the mode toggle button at the top right
mode_button = ctk.CTkButton(app, image=moon_image, text="", command=toggle_mode)
mode_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)  # Adjust 'x' and 'y' to position the button properly

# Binding the wrap_feedback function to the configure event of the app
app.bind("<Configure>", wrap_feedback)

app.mainloop()
