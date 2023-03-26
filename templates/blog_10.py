"""
Program: blog_10
Creation Data: 03/12/2023
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Using a  PanedWindow to create a slide out menu

Description: Use a PanedWindow to create a slide out left menu and
                display 'page content in right pane.

Previous code: blog_4 available on github

Changes: 

"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PageFrm(tk.Frame): 
    # Container frame for page content
    def __init__(self, parent):
        super().__init__(parent)

        # Class constant(s)
        self.TITLE_FONT = ("Helvetica", 12, "bold")
        self.HEADER_FONT = ("Helvetica", 16, "bold")

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_paned_window_frame(self, 'Screen Frame', 1)

    def create_paned_window_frame(self, parent:tk.Frame, text:str = '', bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates content frame for page header and paned window
        Param: parent  - Container widget into which frame is placed
        Param: text    - Label text for frame, default is null (no text)
        Param: bdwidth - Width of frame border, default is 0 (no border)
        Return: frame  - grid-based frame (parent must use grid for geometry manager)
        """
        # Define and place the widget
        frame = tk.LabelFrame(parent, text=text)
        frame.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)
        frame.configure(borderwidth=bdwidth)

        #  Configure layout proportions for inside frame 
        self.set_col_proportions(frame, (1, ))
        self.set_row_proportions(frame, (1, 6))

        # Create header frame for menu button and title
        header_frm = tk.Frame(frame, height=50, width=400)
        header_frm.grid(column=0, row=0, sticky=tk.EW)
        header_frm.columnconfigure(0, weight=1)
        header_frm.columnconfigure(1, weight=8)
        header_frm.rowconfigure(0, weight=1)

        # Create menu button
        self.menu_btn = tk.Button(header_frm, text='☰', bd=0, 
                                  command=lambda: self.show_menu(self.pane))
        self.menu_btn.grid(column=0, row=0)

        # Create application header title
        header_lbl = tk.Label(header_frm, text='Tkinter Demo', 
                              font=self.HEADER_FONT)
        header_lbl.grid(column=1, row=0, sticky=tk.EW)

        # Create main pane window
        self.pane = tk.PanedWindow(frame, bd=2, bg='grey', orient=tk.HORIZONTAL, 
                                   height=250, width=400, relief=tk.FLAT)
        self.pane.grid(column=0, row=1,  sticky=tk.N)

        # Create frame for left pane content and add to main pane window
        self.left_frm = tk.Frame(self.pane)
        self.pane.add(self.left_frm)

        # Create frame for right pane content and add to main pane window
        self.right_frm = tk.Frame(self.pane)
        self.pane.add(self.right_frm)

        # Initial right pane display
        self.content_frm = tk.Frame(self.right_frm)
        self.content_frm.pack()
        self.content_frm.columnconfigure(1, weight=1)
        self.content_frm.rowconfigure(0, weight=1)
        opening_lbl = tk.Label(self.content_frm, text='Welcome to the \n PanelWindow Demo!')
        opening_lbl.grid(column=0, row=0, pady=30)

        return frame

    def set_row_proportions(self, parent:tk.Frame, weights:tuple[int]) -> None:
        """
        Description: Create one or more rowconfigure() statements
        Param: parent  - the frame to which the method refers
        Param: weights - The weight value(s) for the row
        Returns: None
        """
        for row, weight in enumerate(weights):
            parent.rowconfigure(row, weight = weight)

    def set_col_proportions(self, parent:tk.Frame, weights:tuple[int]) -> None:
        """
        Description: Create one or more columnconfigure() statements
        Param: parent  - the frame to which the method refers
        Param: weights - The weight value(s) for the column
        Returns: None
        """
        for col, weight in enumerate(weights):
            parent.columnconfigure(col, weight = weight)

    def show_menu(self, pane:ttk.PanedWindow) -> None:
        """
        Description: Create menu and adjust sash to display
        Param: pane  - pane window that has the pane
        Returns: None
        """
        # Move sash to display left menu button
        pane.sash_place(0, x=75, y=1)
        # Create left menu buttons
        left_btn_1 = ttk.Button(self.left_frm, text='Content 1', 
                                command=self.create_content_1)
        left_btn_1.pack(pady=(10, 5))
        left_btn_2 = ttk.Button(self.left_frm, text='Content 2', 
                                command=self.create_content_2)
        left_btn_2.pack()
        # Reset header menu button 'hide' left menu slider
        self.menu_btn.configure(text='X', 
                                command=lambda: self.hide_menu(self.pane))


    def hide_menu(self, pane:ttk.PanedWindow) -> None:
        """
        Description: Remove buttons in left menu slider and reset sash
        Param: pane  - pane window that has the pane
        Returns: None
        """
        # Move sash back to left edge
        pane.sash_place(0, x=2, y=1)
        # Remove left menu buttons
        for button in self.left_frm.winfo_children():
            button.destroy()
        # Reset header menu button 'show' left menu slider 
        self.menu_btn.configure(text='☰', 
                                command=lambda: self.show_menu(self.pane))

    def create_content_1(self) -> None:
        """
        Description: First display for right pane
        Returns: None
        """
        self.content_frm.destroy()
        self.content_frm = tk.Frame(self.right_frm)
        self.content_frm.pack()

        self.content_frm.columnconfigure(1, weight=1)
        self.content_frm.rowconfigure(0, weight=1)
        self.content_frm.rowconfigure(1, weight=1)

        title_lbl = tk.Label(self.content_frm, text='-- Pane Title One --', 
                             font=self.TITLE_FONT)
        title_lbl.grid(column=0, row=0, pady=(30, 5))
        title_lbl = tk.Label(self.content_frm, text='-- Pane Content 1 Here --')
        title_lbl.grid(column=0, row=1, pady=(10, 5))

    def create_content_2(self) -> None:
        """
        Description: Second display for right pane
        Returns: None
        """
        self.content_frm.destroy()
        self.content_frm = tk.Frame(self.right_frm)
        self.content_frm.pack()

        self.content_frm.columnconfigure(1, weight=1)
        self.content_frm.rowconfigure(0, weight=1)
        self.content_frm.rowconfigure(1, weight=1)

        title_lbl = tk.Label(self.content_frm, text='-- Pane Title Two --', 
                             font=self.TITLE_FONT)
        title_lbl.grid(column=0, row=0, pady=(30, 5))
        title_lbl = tk.Label(self.content_frm, text='-- Pane Content 2 Here --')
        title_lbl.grid(column=0, row=1, pady=(10, 5))


class App(tk.Tk):  
    # Inheriting from Tk class
    def __init__(self):
        super().__init__()  # Initializing the inherited class

        # Program Info
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 300

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate offset to center window on screen
        x_offset = int((screen_width - WINDOW_WIDTH)/2)
        y_offset = int((screen_height - WINDOW_HEIGHT)/2)

        # Define application properties
        self.title('Class Based GUI')
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_offset}+{y_offset}')
        self.iconbitmap(self, default='templates/wolftrack.ico')
        self.resizable(width = False, height = False)
        
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Add content frame to application
        PageFrm(self).grid(sticky = tk.NSEW)


def main():
    prog_app = App()
    prog_app.mainloop()

if __name__ == '__main__': main()
