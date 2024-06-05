import customtkinter as ctk
from tkinter import StringVar
from PIL import Image, ImageTk
import re
import tkinter as tk

# Class to handle theme toggling between dark and light modes
class ThemeToggle:
    def __init__(self, parent_frame, dark_mode_img_path, light_mode_img_path):
        # Initialize with dark mode
        self.is_dark_mode = True
        self.parent_frame = parent_frame

        # Load and resize images for dark and light modes
        self.moon_img = ImageTk.PhotoImage(Image.open(dark_mode_img_path).resize((30, 30), Image.LANCZOS))
        self.sun_img = ImageTk.PhotoImage(Image.open(light_mode_img_path).resize((30, 30), Image.LANCZOS))

        # Create a label to display the current theme icon
        self.icon_label = tk.Label(parent_frame, image=self.moon_img, cursor="hand2")
        # Place at top right corner with padding
        self.icon_label.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
        # Bind click event to toggle theme
        self.icon_label.bind("<Button-1>", self.toggle_mode)

        # Set initial theme colors
        self.set_theme_colors(dark_mode=True)

    def toggle_mode(self, event=None):
        # Toggle between dark and light modes
        if self.is_dark_mode:
            ctk.set_appearance_mode("Light")  # Set light mode
            self.icon_label.configure(image=self.sun_img)  # Change icon to sun
            self.set_theme_colors(dark_mode=False)  # Update theme colors
        else:
            ctk.set_appearance_mode("Dark")  # Set dark mode
            self.icon_label.configure(image=self.moon_img)  # Change icon to moon
            self.set_theme_colors(dark_mode=True)  # Update theme colors
        self.is_dark_mode = not self.is_dark_mode  # Toggle the mode state

    def set_theme_colors(self, dark_mode):
        # Set text color based on the theme
        fg_color = "#ffffff" if dark_mode else "#000000"
        for widget in self.parent_frame.winfo_children():
            # Update text color for different widget types, excluding the feedback label
            if isinstance(widget, (ctk.CTkLabel, ctk.CTkEntry)) and widget != feedback_label:
                widget.configure(text_color=fg_color)

# Class to handle the password visibility toggle
class PasswordToggle:
    def __init__(self, parent_frame, password_entry, hide_img_path, show_img_path):
        # Initialize with password hidden
        self.is_password_visible = False
        self.parent_frame = parent_frame
        self.password_entry = password_entry

        # Load and resize images for hiding and showing the password
        self.hide_img = ImageTk.PhotoImage(Image.open(hide_img_path).resize((30, 30), Image.LANCZOS))
        self.show_img = ImageTk.PhotoImage(Image.open(show_img_path).resize((30, 30), Image.LANCZOS))

        # Create a label to display the current visibility icon
        self.icon_label = tk.Label(parent_frame, image=self.hide_img, cursor="hand2")
        # Add some padding to the left to create space between the icon and the entry field
        self.icon_label.pack(side=tk.LEFT, padx=(5, 0))
        # Bind click event to toggle visibility
        self.icon_label.bind("<Button-1>", self.toggle_password_visibility)

    def toggle_password_visibility(self, event=None):
        # Toggle between showing and hiding the password
        if self.is_password_visible:
            self.password_entry.configure(show="*")  # Hide the password
            self.icon_label.configure(image=self.hide_img)  # Change icon to hide
        else:
            self.password_entry.configure(show="")  # Show the password
            self.icon_label.configure(image=self.show_img)  # Change icon to show
        self.is_password_visible = not self.is_password_visible  # Toggle the visibility state

# Function to check the strength of the input password
def check_password_strength():
    password = password_var.get()  # Get the input password
    
    # Check if password input is empty
    if not password:
        feedback_label.configure(text="Please input a password", text_color="red")
        return

    strength = 0
    feedback = []

    # Criteria for password strength
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

    display_feedback(strength, feedback)  # Display the password strength feedback

# Function to display feedback based on password strength
def display_feedback(strength, feedback):
    if strength == 5:
        feedback_label.configure(text="Password is very strong!", text_color="green")
    elif strength >= 3:
        feedback_label.configure(text="Password is moderate. " + " ".join(feedback), text_color="orange")
    else:
        feedback_label.configure(text="Password is weak. " + " ".join(feedback), text_color="red")

# Function to wrap feedback text based on window size
def wrap_feedback(event):
    feedback_label.configure(wraplength=app.winfo_width() - 40)

# Function to set up the GUI
def setup_gui():
    # Set appearance and theme of the CustomTkinter application
    ctk.set_appearance_mode("System")  # Set appearance mode (System, Dark, Light)
    ctk.set_default_color_theme("blue")  # Set the color theme

    global app, feedback_label
    app = ctk.CTk()  # Initialize the main window
    app.title("Password Strength Checker")  # Set window title
    app.geometry("400x300")  # Set window size

    # Create a main frame to hold all widgets
    main_frame = ctk.CTkFrame(app, width=380, height=280)
    main_frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the main frame
    main_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    # Variable to hold the password input
    global password_var, password_entry
    password_var = StringVar()
    
    # Frame to hold password entry and visibility toggle
    password_frame = ctk.CTkFrame(main_frame)
    password_frame.pack(pady=(60, 20))

    password_entry = ctk.CTkEntry(password_frame, textvariable=password_var, width=260, show="*")  # Reduced width to accommodate the icon
    password_entry.pack(side=tk.LEFT)

    # Add the password visibility toggle functionality
    password_toggle = PasswordToggle(password_frame, password_entry, "images/hide.png", "images/show.png")

    # Button to check password strength
    check_button = ctk.CTkButton(main_frame, text="Check Password Strength", command=check_password_strength)
    check_button.pack(pady=5)

    # Label to display feedback
    feedback_label = ctk.CTkLabel(main_frame, text="", wraplength=360)
    feedback_label.pack(pady=10)

    # Add the theme toggle functionality
    theme_toggle = ThemeToggle(main_frame, "images/moon.png", "images/sun.png")

    # Bind the wrap_feedback function to window resize events
    app.bind("<Configure>", wrap_feedback)

    # Start the application's main event loop
    app.mainloop()

# Run the GUI setup
if __name__ == "__main__":
    setup_gui()
