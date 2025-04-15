import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyautogui  # To get cursor position
import keyboard
import threading
from global_root import set_root, get_root
import global_root
from timer_func import start_timer
from timer_prompt import open_timer_prompt
from settings_func import change_settings
from update_func import update_settings
import time

# initialize variables for screen size
screen_width = 0
screen_height = 0

# Initialize center coordinates for user's screen
screen_center_x = 0
screen_center_y = 0

wodget_open = False
last_keybind_activation = 0
hotkey_ref = None

# Define behavior of buttons
def on_settings_click():
    change_settings()
    
def on_timer_click():
    open_timer_prompt()

def on_exit_click():
    messagebox.showinfo("Exit Program", "Exiting...")
    root.destroy()

# Create the main application window
root = tk.Tk()

root.geometry("400x400")
root.overrideredirect(True)
root.attributes("-transparentcolor", "white")
root.configure(bg="white")  # Color to be treated as transparent
root.withdraw()  # Start hidden

# Target position for the hidden window
target_x, target_y = 0, 20  # Adjust this to the desired position
proximity_radius = 200  # Distance within which the window will appear
proximity_radius_center = 300

# Position the window
root.geometry(f"+{target_x}+{target_y}")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white", highlightthickness=0)
canvas.pack()

# Add a circular image (logo)
image = Image.open("logo4.png").resize((200, 200))  # Replace with your logo path
circle_image = ImageTk.PhotoImage(image)
canvas.create_image(200, 200, image=circle_image)

# Create a label for the title
title_label = tk.Label(
    root,
    text="The Wodget",
    font=("Arial", 22),  # Font and size
    fg="white",  # Text color
    bg="black"
)

# Center the label in the window
title_label.place(relx=0.5, rely=0.5, anchor="center")
title_label.lift()

# Add buttons around the circular logo
button_settings = tk.Button(root, text="⚙", command=on_settings_click, bg="blue", fg="white", font=("Arial", 16))
button_exit = tk.Button(root, text="❌", command=on_exit_click, bg="green", fg="white", font=("Arial", 16))
button_timer = tk.Button(root, text="⏰", command=on_timer_click, bg="orange", fg="white", font=("Arial", 16))

# Position buttons
button_settings.place(x=175, y=57)  # Above the logo
button_exit.place(x=176, y=302)     # Below the logo
button_timer.place(x=53, y=180)     # Left of the logo

# Center coordinates of the circular logo (adjust based on the window size and logo size)
logo_center_x = target_x + 200  # Add half the window width (400/2)
logo_center_y = target_y + 200  # Add half the window height (400/2)

# set user screen size in global values
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
global_root.set_screen_width(screen_width)
global_root.set_screen_height(screen_height)

# Center coordinates for user's screen
screen_center_x = screen_width / 2
screen_center_y = screen_height / 2

def check_cursor_wodget():
    if global_root.get_hover() and not global_root.get_prompt_state():  # Only check if prompt is not open and hover is on
        cursor_x, cursor_y = pyautogui.position()
        distance = ((cursor_x - logo_center_x)**2 + (cursor_y - logo_center_y)**2)**0.5
        #print(f"Distance is currently: {distance}")
        if distance < proximity_radius:
            root.lift()  # Bring window to the front
            root.attributes("-topmost", True)# Ensure it stays above all others
            root.deiconify()
        else:
            root.withdraw()
    root.after(100, check_cursor_wodget)

print(f"Screen Center X: {screen_center_x}")
print(f"Screen Center Y: {screen_center_y}")

# Check for keybind setting and update accordingly
def toggle_visibility():
    global last_keybind_activation
    current_time = time.time()
    global wodget_open
    
    if current_time - last_keybind_activation >= 0.25:
        last_keybind_activation = current_time
        if(wodget_open == True):
            root.withdraw()
            wodget_open = False
        else:
            root.lift()                        # Bring window to the front
            root.attributes("-topmost", True)  # Ensure it stays above all others
            root.deiconify()
            wodget_open = True

def check_settings():
    update = update_settings()
    global hotkey_ref
    #print(update)
    #print(f"Hover is currently: {global_root.get_hover()}")
    if(update == 1):
        global_root.set_hover(False)
        if hotkey_ref is None:
            hotkey_ref = keyboard.add_hotkey('alt+w', toggle_visibility)
    else:
        global_root.set_hover(True)
        if hotkey_ref is not None:
            keyboard.remove_hotkey(hotkey_ref)
            hotkey_ref = None
    root.after(1000, check_settings)

# Start the proximity check loop
check_cursor_wodget()

# start checking settings
check_settings()

# set global_root
global_root.set_root(root)

# set global title object
global_root.set_title(title_label)

# Run the application
root.mainloop()