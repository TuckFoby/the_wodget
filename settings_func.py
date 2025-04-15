import tkinter as tk
from tkinter import messagebox
from tkinter import HORIZONTAL
import global_root

# initialize variables for screen size
screen_width = 0
screen_height = 0

# Initialize center coordinates for user's screen
#screen_center_x = 0
#screen_center_y = 0

def change_settings():
    #settings button clicked
    #prompt window holding all settings fields with fields pre-filled with current settings
    #when submit button is pressed, update settings in a long-term manner (i.e. .txt file lol)
    #if x button is pressed, exit without updates

    # Create a Toplevel window (prompt box)
    root = global_root.get_root()

    prompt_window = tk.Toplevel(root)
    prompt_window.title("Settings")

    # Set the size of the prompt window
    window_width = 350
    window_height = 350

    # get user screen_width and screen_height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the center position for prompt window
    center_x = int((screen_width / 2) - (window_width / 2))
    center_y = int((screen_height / 2) - (window_height / 2))

    # Set the geometry of the prompt window
    prompt_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    prompt_window.transient(root)                  # Keep it on top of the root window
    prompt_window.grab_set()                       # Disable interaction with the main window

    # begin checking for cursor proximity to prompt window
    isOpen = global_root.get_prompt_state()
    if(isOpen == False):
        global_root.set_prompt_state(True)
        print(f"Prompt state set: {isOpen}")
    
    # Label and input for keybind setting
    tk.Label(prompt_window, text="Enable Keybind (Default: On-Hover Overlay)", font=("Arial", 12)).pack(pady=10)
    # Options for the dropdown menu
    keybind_options = ["Default", "ALT-W"]

    # Create a Tkinter variable to store the selected keybind
    keybind_var = tk.StringVar()
    
    keybind = 0
    
    with open("settings.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        if "ALT-W" in line:
            keybind = 1 
            
    keybind_var.set(keybind_options[keybind])       # Set starting value for menu
    
    # Create the OptionMenu (dropdown) widget
    keybind_menu = tk.OptionMenu(prompt_window, keybind_var, *keybind_options)
    keybind_menu.pack(pady=10)
    
    # Label and input for timer audio setting
    tk.Label(prompt_window, text="Alarm Sound for Timer", font=("Arial", 12)).pack(pady=10)
    # Options for the dropdown menu
    audio_options = ["Default", "Gura", "Mococo"]
    
    # Create a Tkinter variable to store the selected keybind
    audio_var = tk.StringVar()
    
    audio = 0
    
    for line in lines:
        if "Gura" in line:
            audio = 1
        elif "Mococo" in line:
            audio = 2
    
    audio_var.set(audio_options[audio])              # Set starting value for menu
    
    # Create the OptionMenu (dropdown) widget
    audio_menu = tk.OptionMenu(prompt_window, audio_var, *audio_options)
    audio_menu.pack(pady=10)
    
    # Create slider for volume control
    volume = 50
    
    volume_found = False

    for line in lines:
        if line.startswith("Volume: "):
            volume = int(line.split("Volume: ")[1].strip())
            break
    
    volume_slider = tk.Scale(
        prompt_window,
        from_=0,
        to=100,
        orient=tk.HORIZONTAL,
        length=300,
        label="Volume",
    )
    
    volume_slider.set(volume)

    volume_slider.pack(pady=20)
    
    global_root.set_root(root)
    
    # Function to handle submit button press
    def handle_submit():
        keybind_input = keybind_var.get()
        print(f"User selected keybind: {keybind_input}")
        
        audio_input = audio_var.get()
        
        volume_input = volume_slider.get()
        
        # Save the selected keybind to a settings.txt file
        with open("settings.txt", "w") as file:
            file.write(f"Keybind: {keybind_input}\n")
            file.write(f"Audio: {audio_input}\n")
            file.write(f"Volume: {volume_input}")

        messagebox.showinfo("Success","Settings Saved")
        prompt_window.destroy()                      # Close the prompt window
        isOpen = global_root.get_prompt_state()
        if(isOpen == True):
            global_root.set_prompt_state(False)
            print(f"Prompt state set: {isOpen}")
            
    # Submit button
    submit_button = tk.Button(prompt_window, text="Submit", command=handle_submit, font=("Arial", 12))
    submit_button.pack(pady=10)
    