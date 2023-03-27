"""
Program: Main 1
Creation Data: 03/27/2023
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: 

Description: Post part of a series on creating a point of sales system
            using Python's Tkinter module. 

            - Create a splash page for app

Previous code: blog_7 available on github
""" 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Page1(tk.Frame): 
    # Container frame for page content
    def __init__(self, parent, controller):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Provide navigation and access to page data
        self.ctrl = controller

        # Class constant(s)
        self.TITLE_FONT = ("Helvetica", 16, "bold")

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_splash_frame(self, '', 1)

    def create_splash_frame(self, parent:tk.Frame, text:str = '', bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates grid-based LabelFrame
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
        self.set_row_proportions(frame, (1, 1))

        # Create and place two Label widgets
        title_lbl = tk.Label(frame, text = 'Point of Sales', 
                             font=self.TITLE_FONT, foreground='#44271f')
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)

        self.coffee_img = tk.PhotoImage(file='coffee_shoppe\coffee_splash_sm.png')
        img_lbl = tk.Label(frame, image=self.coffee_img)
        img_lbl.grid(column = 0, row = 1,pady=(0, 10), sticky = tk.EW)
        
        page_btn = ttk.Button(frame, text = 'Login', width = 10,
            command=lambda: self.ctrl.show_frame('Page2') )
        page_btn.grid(column = 0, row = 2,pady=(30, 20), sticky = tk.N)

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


class Page2(tk.Frame): 
    # Container frame for page content
    def __init__(self, parent, controller):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Provide navigation and access to page data
        self.ctrl = controller

        # Class constant(s)
        self.TITLE_FONT = ("Helvetica", 16, "bold")

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_grid_frame(self, 'Screen Frame', 1)

    def create_grid_frame(self, parent:tk.Frame, text:str = '', bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates grid-based LabelFrame
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
        self.set_row_proportions(frame, (1, 1))

        # Create and place two Label widgets
        title_lbl = tk.Label(frame, text = '-- Page 2 --', font=self.TITLE_FONT)
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)
        page_btn = ttk.Button(frame, text = 'Page 1', width = 10,
            command=lambda: self.ctrl.show_frame('Page1') )
        page_btn.grid(column = 0, row = 1,pady=(30, 20), sticky = tk.N)

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


class App(tk.Tk):  
    def __init__(self):
        super().__init__()  

        # Update tuple with Page classes to be 
        # added to frames dictionary
        self.PAGES = (Page1, Page2)  

        # Program Constants
        WINDOW_WIDTH = 405
        WINDOW_HEIGHT = 375

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate offset to center window on screen
        x_offset = int((screen_width - WINDOW_WIDTH)/2)
        y_offset = int((screen_height - WINDOW_HEIGHT)/2)

        # Define application properties
        self.title('Wolf Moon Coffee Shoppe')
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_offset}+{y_offset}')
        self.iconbitmap(self, default='coffee_shoppe\coffee1.ico')
        self.resizable(width = False, height = False)
        
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Create a dictionary of frames
        self.frames = {}

        # Add page frames to the dictionary.
        for pg_frm in self.PAGES:
            # Creates key word string from page class name
            page_name = pg_frm.__name__
            # Creates instance of page class
            frame = pg_frm(parent=self, controller=self)
            # Adds key value pair to dictionary
            self.frames[page_name] = frame
            # Places frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Display menu bar
        self.create_menu_bar(self)

        # Display the page
        self.show_frame('Page1')

    def create_menu_bar(self, main_win: tk.Tk) -> None:
        '''
        Description: Dynamic menu bar display option based 
                    on if use is logged in
        Param: main_win - main application window that contains the menu bar
        Return: None
        '''

        # Create menu bar
        self.menu_bar = tk.Menu(main_win)

        # Create Page menu
        page_menu = tk.Menu(self.menu_bar, tearoff=0)

        # Create Pages menu items
        page_menu.add_command(label='Page 1', command=lambda: self.show_frame('Page1'))
        page_menu.add_command(label='Page 2', command=lambda: self.show_frame('Page2'))


        # Create Exit menu item
        page_menu.add_separator()
        page_menu.add_command(label='Exit', command=self.quit)

        # Add Pages menu and menu items to the menu bar
        self.menu_bar.add_cascade(label='Pages', menu=page_menu)

        # Create options for Help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)

        # Create Help menu item and add menu and menu item to menu bar
        help_menu.add_command(label='Help', command=self.help)
        self.menu_bar.add_cascade(label='Help', menu=help_menu)

        # Assign menu bar to the window
        self.config(menu=self.menu_bar)

    def help(self) -> None:
        """
        Description: Displays Help pop-up window
        Param: 
        Return None
        """
        messagebox.showinfo(
            'Help', 'Do you really need help with this program?')

    def show_frame(self, page_name:str) -> None:
        """
            Description: Displays specified page frame
            Param:  page_name - name of page in frames dictionary
            Return: None
        """
        frame = self.frames[page_name]
        frame.tkraise()


def main():
    prog_app = App()
    prog_app.mainloop()

if __name__ == '__main__': main()
