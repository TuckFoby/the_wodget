# global variable
global_root = None
global_title = None
global_prompt_state = False 
global_screen_width = None
global_screen_height = None
global_hover = None

def set_root(root):
    global global_root
    global_root = root

def get_root():
    return global_root

def set_title(title):
    global global_title
    global_title = title

def get_title():
    return global_title

def set_prompt_state(isOpen):
    global global_prompt_state
    global_prompt_state = isOpen

def get_prompt_state():
    return global_prompt_state

def set_screen_width(width):
    global global_screen_width
    global_screen_width = width

def get_screen_width():
    return global_screen_width

def set_screen_height(height):
    global global_screen_height
    global_screen_height = height

def get_screen_height():
    return global_screen_height

# def set_keybind(keybind):
#     global global_keybind
#     global_keybind = keybind

# def get_keybind():
#     return global_keybind

def set_hover(hover):
    global global_hover
    global_hover = hover
    
def get_hover():
    return global_hover