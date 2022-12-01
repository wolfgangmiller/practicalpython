"""
Program: blog_1
Creation Data: 11/27/2022
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Creating a Class-based Python Tkinter Template - Part 2

Description: Post part of a series on creating a class-based GUI
            using Python's Tkinter module.

Previous code: blog_1 available on github

Changes: 12/01/2022 - This version centers the window, add a favicon to the title bar, 
            and control window resizing. 
"""


import tkinter as tk
from tkinter import ttk  # Note used in this example

class App(tk.Tk):  # Inheriting from Tk class
    # Initializing the App class
    def __init__(self):
        # Initializing the inherited class
        super().__init__()

        # Define program constants
        WIDTH = 300
        HEIGHT = 100 

        # Get the width and height of screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight() 

        # Calculate offset to center window on screen
        x_offset = int((screen_width/2) - (WIDTH/2))
        y_offset = int((screen_height/2) - (HEIGHT/2)) 

        # Define application properties
        self.title('Class Based GUI') # sets title
        self.iconbitmap(default='wolftrack.ico') # sets favicon
        # Sets window size and centers on screen
        self.geometry(f'{WIDTH}x{HEIGHT}+{x_offset}+{y_offset}') 
        # Set App window resizing options (width, height)
        self.resizable(False,True)

def main():
    # Creates instance of App class
    prog_app = App()
    # Runs program until closed
    prog_app.mainloop()

# Check if program
if __name__ == '__main__': main()

