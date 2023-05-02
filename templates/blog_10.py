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

Changes: 04/29/2023 - Update path to favicon after move to templates folder
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PageFrm(tk.Frame): 
    # Container frame for page content
    def __init__(self, parent):
        super().__init__(parent)

        # Configure style
        self.style = ttk.Style(self)
        self.style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'))
        self.style.configure('Title.TLabel', font=('Helvetica', 12, 'bold'))
        self.style.configure('Pane.TPanedwindow', background='lightgray')
        self.style.configure("Sash", sashthickness=2)

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_paned_window_frame(self, 'Screen Frame', 1)

        # Bind pane sash to motion event
        self.pane.bind('<Motion>', lambda event: self.pane_max_size())

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_paned_window_frame(self, parent:tk.Frame, text:str = '', bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates content frame for page header and paned window
        Param: parent  - Container widget into which frame is placed
        Param: text    - Label text for frame, default is null (no text)
        Param: bdwidth - Width of frame border, default is 0 (no border)
        Return: frame  - grid-based frame (parent must use grid for geometry manager)
        """
        # Define and place the widget
        frame = ttk.LabelFrame(parent, text=text)
        frame.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)
        frame.configure(borderwidth=bdwidth)

        #  Configure layout proportions for inside frame 
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform=True)

        # Create header frame for menu button and title
        # header_frm = ttk.Frame(frame, height=50, width=400)
        header_frm = ttk.Frame(frame, height=50)
        header_frm.grid(column=0, row=0, sticky=tk.EW)
        header_frm.columnconfigure(0, weight=1)
        header_frm.columnconfigure(1, weight=8)
        header_frm.rowconfigure(0, weight=1)

        # Create menu button
        self.menu_btn = tk.Button(header_frm, text='☰', bd=0, 
                                  command=lambda: self.show_menu(self.pane))
        self.menu_btn.grid(column=0, row=0)

        # Create application header title
        header_lbl = ttk.Label(header_frm, text='PanedWindow Demo', 
                              style='Header.TLabel')
        header_lbl.grid(column=1, row=0, sticky=tk.N)

        # Create frame with border for paned window
        pane_frm = ttk.Frame(frame, borderwidth=2, relief=tk.SOLID)
        pane_frm.grid(column=0, row=1, rowspan=6, sticky=tk.EW)
        pane_frm.columnconfigure(0, weight=1)
        pane_frm.rowconfigure(0, weight=1)

        # Create main pane window
        self.pane = ttk.PanedWindow(pane_frm, orient=tk.HORIZONTAL, 
                                   height=250, width=400, style='Pane.TPanedwindow')
        self.pane.grid(column=0, row=1, sticky=tk.N)

        # Create frame for left pane content and add to main pane window
        self.left_frm = ttk.Frame(self.pane)
        self.pane.add(self.left_frm)

        # Create frame for right pane content and add to main pane window
        self.right_frm = ttk.Frame(self.pane)
        self.pane.add(self.right_frm)

        # Initial right pane display
        self.content_frm = ttk.Frame(self.right_frm)
        self.content_frm.pack()
        self.content_frm.columnconfigure(1, weight=1)
        self.content_frm.rowconfigure(0, weight=1)
        opening_lbl = ttk.Label(self.content_frm, 
                                text='Welcome to the Panel Window Demo!',
                                wraplength=100,
                                justify=tk.CENTER)
        opening_lbl.grid(column=0, row=0, pady=30, sticky=tk.N)

        return frame

    def pane_max_size(self) -> None:
        if self.pane.sashpos(0) != 75:
            self.pane.sashpos(0, newpos=75)
    
    def show_menu(self, pane:ttk.PanedWindow) -> None:
        """
        Description: Create menu and adjust sash to display
        Param: pane  - pane window that has the pane
        Returns: None
        """
        # Move sash to display left menu button
        pane.sashpos(0, newpos=75)

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
        pane.sashpos(0, newpos=0)

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
        self.content_frm = ttk.Frame(self.right_frm)
        self.content_frm.pack()

        self.content_frm.columnconfigure(1, weight=1)
        self.content_frm.rowconfigure((0, 1), weight=1)

        title_lbl = ttk.Label(self.content_frm, text='-- Pane Title One --', 
                                style='Title.TLabel')                            
        title_lbl.grid(column=0, row=0, pady=(30, 5))
        title_lbl = ttk.Label(self.content_frm, text='-- Pane Content 1 Here --')
        title_lbl.grid(column=0, row=1, pady=(10, 5))

    def create_content_2(self) -> None:
        """
        Description: Second display for right pane
        Returns: None
        """
        self.content_frm.destroy()
        self.content_frm = ttk.Frame(self.right_frm)
        self.content_frm.pack()

        self.content_frm.columnconfigure(1, weight=1)
        self.content_frm.rowconfigure((0, 1), weight=1)

        title_lbl = ttk.Label(self.content_frm, text='-- Pane Title Two --', 
                             style='Title.TLabel')
        title_lbl.grid(column=0, row=0, pady=(30, 5))
        title_lbl = ttk.Label(self.content_frm, text='-- Pane Content 2 Here --')
        title_lbl.grid(column=0, row=1, pady=(10, 5))


class App(tk.Tk):  
    # Inheriting from Tk class
    def __init__(self):
        super().__init__()  # Initializing the inherited class

        # Program Info
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 320

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
        PageFrm(self)


def main():
    prog_app = App()
    prog_app.mainloop()

if __name__ == '__main__': main()
