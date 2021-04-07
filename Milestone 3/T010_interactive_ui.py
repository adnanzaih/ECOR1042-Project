#P5 Task 2 Text-Based Interface
#T010 Vincent Chen, Adnan Hafeez, Logan Delaat, Ayesha Dassanayake

from T010_image_filters import *
from Cimpl import *
    
def execute()-> Image:
    """
    Displays a menu of options for the user to choose from.
    Returns either an image if the user enters a sequence of options with no errors, 
    or it returns a statement telling the user has entered an error.
    
    >>>execute()
    """
    
    options = "L)oad Image    S)ave-as \n3)-tone    X)treme contrast    T)int sepia    P)osterize \nE)dge detect    D)raw curve    V)ertical flip    H)orizontal flip \nQ)uit \n:"
    valid_commands = {'L','S','3','X',"T","P","E","D","V","H","Q"}
    valid_filters = {'X':extreme_contrast,"T":sepia_filter,"P":posterize,"V":flip_vertical,"H":flip_horizontal}
    print(options)    
    command = ""
    load_img = []
    
    while command.upper() != "Q":
        command = ""
        command = input()
        
        if command.upper() == "L":
            load_img = load_image(choose_file())
            command = ""
            
        if bool(load_img) == True: #image is loaded
            if command.upper() == "E":
                threshold = input("Please input a threshold value between 0-255: ")
                load_img = detect_edges(load_img, int(threshold))
                show(load_img)
                
            elif command.upper() == "D":
                load_img = draw_curve(load_img,"lemon", pointList=None)[0]
                show(load_img)
                
            elif command.upper() == "3":
                load_img = three_tone(load_img,"aqua","blood","lemon")
                show(load_img)
                
            elif command.upper() in valid_filters:
                load_img = valid_filters[command.upper()](load_img)
                show(load_img)
                
            elif command.upper() == "S":
                save_as(load_img)
                
            elif command.upper() not in valid_commands:
                if command != "":
                    print("no such command")
                    
        if bool(load_img) == False:
            if command.upper() in valid_commands:
                if command.upper() != "Q" or command.upper() != "L":
                    print("No image loaded")
                    
            if command.upper() not in valid_commands:
                print("no such command")

        print(options)
    print("Quitting program")
    
if __name__ == "__main__":
    execute()

