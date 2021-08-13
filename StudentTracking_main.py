# Python Ver:   3.9.6
#
# Author:       Devon Prevost
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import StudentTracking_gui
import StudentTracking_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minmize(700,700) # (Height, Width)
        self.master.maximize(700,700)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,700,700)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: StudentTracking_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        StudentTracking_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()              # This is the syntax that creates the window using Tkinter
    App = ParentWindow(root)    # The syntax required to pass the window to our class
    root.mainloop()             # Must have this loop so window can be consistant on our screen until we close it,
                                # otherwise it disappears immediately
