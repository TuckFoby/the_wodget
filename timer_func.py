import tkinter as tk
from global_root import set_title, get_title
import time
import winsound
import pygame

def start_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds  # Convert input to total seconds
    
    audio = 0
    volume = 0.5
    
    with open("settings.txt", "r") as file:
        lines = file.readlines()
    
    for line in lines:
        if "Gura" in line:
            audio = 1
        elif "Mococo" in line:
            audio = 2
    
    for line in lines:
        if line.startswith("Volume: "):
            # get volume and reduce to a value between 0.0 and 1.0
            volume = (int(line.split("Volume: ")[1].strip())) / 100
            break
    
    print(f"Volume is: {volume}")

    def countdown():
        nonlocal total_seconds  # Allows us to modify the total_seconds variable
        if total_seconds >= 0:
            # Calculate minutes and seconds
            mins = total_seconds // 60
            secs = total_seconds % 60

            # Format the time as MM:SS and update the label
            timer_str = f"{mins:02d}:{secs:02d}"
            title = get_title()
            title.config(text=timer_str)
            set_title(title)

            # Reduce the total time by 1 second and call countdown again after 1 second
            total_seconds -= 1
            time.sleep(1)  # Schedule the next update
            countdown()
        else:
            # When the timer ends, update the label
            title = get_title()
            title.config(text="Time's Up!")
            set_title(title)
            
            alarm(audio, volume)
            
            title.config(text="The Wodget")
            set_title(title)
            return
    countdown()

def alarm(audio, volume):
    if audio == 0:
        # Initialize the mixer
        pygame.mixer.init()
        # Load a sound file (you can generate or use a simple sound file)
        sound = pygame.mixer.Sound("default.mp3")
        # Set volume
        sound.set_volume(volume)
        # Play the audio
        sound.play()
        time.sleep(11)
    elif audio == 1:
        # Initialize the mixer
        pygame.mixer.init()
        # Load a sound file (you can generate or use a simple sound file)
        sound = pygame.mixer.Sound("gura.mp3")
        # Set volume
        sound.set_volume(volume)
        # Play the audio
        sound.play()
        time.sleep(15)
    elif audio == 2:
        # Initialize the mixer
        pygame.mixer.init()
        # Load a sound file (you can generate or use a simple sound file)
        sound = pygame.mixer.Sound("mococo.mp3")
        # Set volume
        sound.set_volume(volume)
        # Play the audio
        sound.play()
        time.sleep(23)