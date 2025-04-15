import global_root
import timer_func
import tkinter as tk
import threading


def open_timer_prompt():
    # get root
    root = global_root.get_root()

    # set user's screen width and height
    screen_width = global_root.get_screen_width()
    screen_height = global_root.get_screen_height()

    # Create a Toplevel window (prompt box)
    prompt_window = tk.Toplevel(root)
    prompt_window.title("Timer Input")

    # Set the size of the prompt window
    window_width = 300
    window_height = 250

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
    
    # Label to ask for input
    tk.Label(prompt_window, text="Please enter the timer amount:", font=("Arial", 12)).pack(pady=10)

    # Label and input field for minutes
    tk.Label(prompt_window, text="Minutes:", font=("Arial", 12)).pack(pady=5)
    minutes_var = tk.StringVar(value="5")
    minutes_input = tk.Entry(prompt_window, textvariable=minutes_var, font=("Arial", 12))  # Create Entry
    minutes_input.pack(pady=5)                     # Pack Entry

    # Label and input field for seconds
    tk.Label(prompt_window, text="Seconds:", font=("Arial", 12)).pack(pady=5)
    seconds_var = tk.StringVar(value="0")
    seconds_input = tk.Entry(prompt_window, textvariable=seconds_var, font=("Arial", 12))  # Create Entry
    seconds_input.pack(pady=5)                     # Pack Entry

    # Function to handle submission
    def handle_submit():
        isOpen = global_root.get_prompt_state()
        if(isOpen):
            global_root.set_prompt_state(False)

        #user_minutes_input = minutes_var.get()
        #user_seconds_input = seconds_var.get()
        
        minutes = 0
        seconds = 0
        try:
            minutes = int(minutes_var.get())  # Ensure input is an integer
            seconds = int(seconds_var.get())  # Ensure input is an integer
        except ValueError:
            messagebox.showinfo("Input invalid! Please try again.")
            return
        
        isOpen = global_root.get_prompt_state()
        if(isOpen == True):
            global_root.set_prompt_state(False)
            print(f"Prompt state set: {isOpen}")
        prompt_window.destroy()                    # Close the prompt box
        
        # Start the timer in a thread
        thread = threading.Thread(target=timer_func.start_timer, args=(minutes, seconds))
        thread.daemon = True
        thread.start()

    # Submit button
    submit_button = tk.Button(prompt_window, text="Submit", command=handle_submit, font=("Arial", 12))
    submit_button.pack(pady=10)
