"""
Program: blog_1
Creation Data: 11/26/2022
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Creating a Class-based Python Tkinter Template – Part 1

Description: First post in a series on creating a class-based GUI
            using Python's Tkinter module.
"""


import tkinter as tk
from tkinter import ttk  # Note used in this example

class App(tk.Tk):  # Inheriting from Tk class
    # Initializing the App class
    def __init__(self):
        # Initializing the inherited class
        super().__init__()   

        # Define application properties
        self.title('Class Based GUI') # sets title
        self.geometry('300x100') # Sets window size

def main():
    # Creates instance of App class
    prog_app = App()
    # Runs program until closed
    prog_app.mainloop()

# Check if program
if __name__ == '__main__': main()

