"""
Program: Main 2
Creation Data: 06/06/2023
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: 

Description: Post part of a series on creating a point of sales system
            using Python's Tkinter module. 

            - Create a login page for app

Previous code: main1.py available on github
""" 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Page1(tk.Frame):      # Splash Page
    # Container frame for page content
    def __init__(self, parent, controller):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Provide navigation and access to page data
        self.ctrl = controller

        # Configure style
        self.style = ttk.Style(self)
        self.style.configure('Splash_Title.TLabel', 
                             font=('Helvetica', 20, 'bold'),
                             foreground='#44271f')

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_splash_frame(self, '', 1)

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_splash_frame(self, parent:tk.Frame, text:str = '', 
                            bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates grid-based LabelFrame
        Param: parent  - Container widget into which frame is placed
        Param: text    - Label text for frame, default is null (no text)
        Param: bdwidth - Width of frame border, default is 0 (no border)
        Return: frame  - grid-based frame (parent must use grid for 
                        geometry manager)
        """
        # Define and place the widget
        frame = ttk.LabelFrame(parent, text=text)
        frame.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)
        frame.configure(borderwidth=bdwidth)

        # Create and place two Label widgets
        title_lbl = ttk.Label(frame, text = 'Point of Sales', 
                             style='Splash_Title.TLabel')
        title_lbl.pack(side=tk.TOP, pady=(20, 0))

        self.coffee_img = tk.PhotoImage(file='coffee_shoppe\coffee_splash_sm.png')
        img_lbl = ttk.Label(frame, image=self.coffee_img)
        img_lbl.pack(side=tk.TOP, expand=True)
        
        page_btn = ttk.Button(frame, text = 'Login', width = 10,
            command=lambda: self.ctrl.show_frame('Page2') )
        page_btn.pack(side=tk.TOP, expand=True)

        return frame


class Page2(tk.Frame):      # Login Page 
    # Container frame for page content
    def __init__(self, parent, controller):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Provide navigation and access to page data
        self.ctrl = controller

        # Create Entry variables
        self.username_str = tk.StringVar()
        self.password_str = tk.StringVar()

        # Define user data 
        self.user = [('maya', '123', 'Maya')]

        # Configure style
        # self.style = ttk.Style(self)
        self.ctrl.style.configure('Title.TLabel', 
                             font=(self.ctrl.TITLE_FONT))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_login_frame(self, 'Login', 1)

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_login_frame(self, parent:tk.Frame, text:str = '', 
                          bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates grid-based LabelFrame
        Param: parent  - Container widget into which frame is placed
        Param: text    - Label text for frame, default is null (no text)
        Param: bdwidth - Width of frame border, default is 0 (no border)
        Return: frame  - grid-based frame (parent must use grid for 
                        geometry manager)
        """
        # Define and place the widget
        frame = ttk.LabelFrame(parent, text=text)
        frame.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)
        frame.configure(borderwidth=bdwidth)

        # Set the grid layout for main frame
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure((0, 1, 2, 3), weight=1) 

        # Create and place login frame
        login_frm = ttk.Frame(frame)
        login_frm.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)

        # Set the grid layout for login frame
        login_frm.columnconfigure((0, 1), weight=1)
        login_frm.rowconfigure((0, 1, 2), weight=1)        
        

        # Create and place username and password widgets
        user_lbl = ttk.Label(login_frm, text='Username: ')
        user_lbl.grid(row=0, column=0, padx=(20, 0), pady=(10, 0), sticky=tk.W)
 
        self.user_ent = ttk.Entry(login_frm, width=20,
                             textvariable=self.username_str)
        self.user_ent.grid(row=0, column=1, pady=(20, 0), sticky=tk.W)
        self.user_ent.focus()

        password_lbl = ttk.Label(login_frm, text='Password: ')
        password_lbl.grid(row=1, column=0, padx=(20, 0), sticky=tk.W)

        self.password_ent = ttk.Entry(
            login_frm, width=20, textvariable=self.password_str, show='*')
        self.password_ent.grid(row=1, column=1, pady=(5, 0), sticky=tk.W)

         # Create and place login button
        login_btn = ttk.Button(login_frm, text='Login', 
                               width=20, command=self.login)
        login_btn.grid(row=2, column=0, padx=(0, 20),
                       pady=(10, 20), columnspan=2, sticky=tk.E)   

        self.instructions_lbl = ttk.Label(frame, text='Enter Username and Password')
        self.instructions_lbl.grid(row=1, column=0, rowspan=3, sticky=tk.N) 

        return frame
    
    def is_valid(self) -> bool:
        '''
        Description: Checks if entered information matches login credentials
        Param: None
        Return: True or False  
        '''           
        return  self.user[0][0].lower() == self.username_str.get().strip().lower() and self.user[0][1] == self.password_str.get().strip()

    def login(self) -> None:
        '''
        Description: Allows access to POS if userID and password are valid
                Updates menu bar and sets barista's nama in Order Entry page
        Param: None
        Return: None  
        '''
        if len(self.user) < 1:
            # Empty list as userID was not found
            success = False
        else:
            # Check if userID and password match
            success = self.is_valid()        

        if success:
            self.emp_name = self.user[0][2]
            self.instructions_lbl.configure(text=f'{self.emp_name} is successfully login')
        else:
            messagebox.showwarning(
                title='Coffee Shoppe Login', message='Invalid userID and/or password!')


class Page3(tk.Frame):      # Order Page 
    # Container frame for page content
    def __init__(self, parent, controller):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Provide navigation and access to page data
        self.ctrl = controller

        # Configure style
        # self.style = ttk.Style(self)
        self.ctrl.style.configure('Title.TLabel', 
                             font=(self.ctrl.TITLE_FONT))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_entry_frame(self, 'Screen Frame', 1)

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_entry_frame(self, parent:tk.Frame, text:str = '', 
                          bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates grid-based LabelFrame
        Param: parent  - Container widget into which frame is placed
        Param: text    - Label text for frame, default is null (no text)
        Param: bdwidth - Width of frame border, default is 0 (no border)
        Return: frame  - grid-based frame (parent must use grid for 
                        geometry manager)
        """
        # Define and place the widget
        frame = ttk.LabelFrame(parent, text=text)
        frame.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)
        frame.configure(borderwidth=bdwidth)

        # Create and place two Label widgets
        title_lbl = ttk.Label(frame, text = '-- Page 3 --', 
                              style='Title.TLabel')
        title_lbl.pack(side=tk.TOP, pady=(20, 0))
        page_btn = ttk.Button(frame, text = 'Page 1', width = 10,
            command=lambda: self.ctrl.show_frame('Page1') )
        page_btn.pack(side=tk.TOP, expand=True)

        return frame


class App(tk.Tk):  
    def __init__(self):
        super().__init__()  

        # Update tuple with Page classes to be 
        # added to frames dictionary
        self.PAGES = (Page1, Page2, Page3)  

        # Program Constants
        WINDOW_WIDTH = 405
        WINDOW_HEIGHT = 375


        self.style = ttk.Style(self)
        self.TITLE_FONT = ('Sans', 12, "bold")

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
        page_menu.add_command(label='Login', command=lambda: self.show_frame('Page2'))
        page_menu.add_command(label='Page 3', command=lambda: self.show_frame('Page3'))


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
