import global_root

def update_settings():
    with open("settings.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        #print("Lines: "+ line)
        if "ALT-W" in line:
            return 1
        elif "On-Hover Overlay + ALT-W" in line:
            return 2
        else:
            return 0