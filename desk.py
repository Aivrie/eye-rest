''' 
Desktop notification - This desktop notifier app runs on your system and sends you a piece of information after a
fixed interval of time 

For this application we will remind user to look away from computer and automatically reduce the brightness of
computer screen.

To increase the brightness of your computer, use the bright_up() function at the bottom of the script

'''

# Step 1: Install the required packages

# Step 2: Import required libraries
import datetime
import time
from plyer import notification
import screen_brightness_control as sb


# Step 2: Create the notifier application
def desk_notify():
    
    # Function to reduce screen brightness
    sb.set_brightness(0)
    current_brightness = sb.get_brightness()
    
    notification.notify(title='Look Away from Your Screen',
                    message='You have been staring at your screen for too long. \nTake a 5 minute break to rest your eyes and prevent eyestrain',
                    app_icon=None,
                    timeout=10,
                    toast=True)
    time.sleep(900)
    
    return current_brightness

desk_notify()


# def bright_on():
#     # Function to reduce screen brightness
#     sb.set_brightness(25)
#     current_brightness = sb.get_brightness()
#     return current_brightness

# bright_on()
    

# Step 3: To make the application run in the background;
# Type 'pythonw.exe .\desk.py' into the command line
