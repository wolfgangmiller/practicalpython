"""
Program: Main 4
Creation Data: 08/206/2023
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: 

Description: Post part of a series on creating a point of sales system
            using Python's Tkinter module. 

            - Create Coffee table in coffee.db 
            - Create layout for Order Entry page

Previous code: main3.py available on github
""" 

import tkinter as tk
import db_utils as dbu
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
        self.create_splash_frame(parent=self, text='', bdwidth=1)

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

        self.user_id = ''
        self.emp_name = ''

        # Define user data
        self.login_db = self.ctrl.LOGIN_DB
        self.coffee_db = self.ctrl.COFFEE_DB

        self.EMP_ID_SQL = """
                SELECT f_name FROM Employees
                WHERE employee_id = ?;
        """
        self.USER_INFO_SQL = """
                SELECT * FROM users
                WHERE user_id = ?;
        """

        self.user = [('maya', '123', 'Maya')]


        # Configure style
        # self.style = ttk.Style(self)
        self.ctrl.style.configure('Title.TLabel', 
                             font=(self.ctrl.TITLE_FONT))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_login_frame(parent=self, text='Login', bdwidth=1)

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

        # Class binds
        self.master.bind('<Return>', lambda event:self.login())

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
        return  self.user_info[0][0].lower() == self.username_str.get().strip().lower() and self.user_info[0][1] == self.password_str.get().strip()

    def clear_login_entries(self) -> None:
        '''
        Description: Clears order entry fields
        Param: None
        Return: None
        '''
        self.user_ent.delete(0, tk.END)
        self.user_ent.focus()
        self.password_ent.delete(0, tk.END)

    def get_emp_name(self, id:int) -> str:
        conn = dbu.create_connection(self.coffee_db)
        name = dbu.get_filtered_records(conn, self.EMP_ID_SQL, 
                                        id,
                                        self.login_db)
        dbu.close_connection(conn, self.coffee_db)
        return name[0][0]

    def login(self) -> None:
        '''
        Description: Allows access to POS if userID and password are valid
                Updates menu bar and sets barista's nama in Order Entry page
        Param: None
        Return: None  
        '''

        # Establish a connection to login database
        conn = dbu.create_connection(self.login_db)

        # Get user info from db if exists
        self.user_info = dbu.get_filtered_records(conn, self.USER_INFO_SQL, 
                                             self.username_str.get().strip().lower(),
                                             self.login_db)

        if len(self.user_info) < 1:
            # Empty list as userID was not found
            success = False
        else:
            # Check if userID and password match
            success = self.is_valid()        

        if success:
            self.emp_name = self.get_emp_name(self.user_info[0][2])
            self.instructions_lbl.configure(text=f'{self.emp_name} is successfully login')

            # Set to update menu bar 
            self.ctrl.logged_in = True
            self.ctrl.create_menu_bar(self.ctrl)
            self.clear_login_entries()
            
        else:
            messagebox.showwarning(
                title='Coffee Shoppe Login', message='Invalid userID and/or password!')

    def logout(self) -> None:
        '''
        Description: Logs out user and restricts access to POS 
                      Updates menu bar 
        Param: None
        Return: None  
        '''
        self.ctrl.logged_in = False
        self.ctrl.create_menu_bar(self.ctrl)
        self.ctrl.show_frame('Page2')    # Login page 


class Page3(tk.Frame):      # Order Page 
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Provide navigation and access to page data
        self.ctrl = controller

        # Configure style
        self.ctrl.style.configure('Title.TLabel', 
                             font=(self.ctrl.TITLE_FONT))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2), weight = 1)


        # Define and place the widget
        # Create page frame sections
        self.create_header_frame(parent=self, 
                                title='Order Entry', 
                                format='Title.TLabel')
        self.create_order_frame(parent=self)
        self.create_total_frame(parent=self)
    
        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_header_frame(self, parent:tk.Frame, title:str, format:str) -> tk.Frame:
        """
        Description: Create header frame section 
        Param: container - Parent grid container
        Param: title     - The frame that holds the widget
        Param: format    - Formatting for header text
        Return: Header frame
        """        
        # Create frame widget
        frame = ttk.Frame(parent)

        # Configure layout proportions for frame
        frame.columnconfigure(0, weight=1, uniform='title')
        frame.columnconfigure(1, weight=2, uniform='title')
        frame.columnconfigure(2, weight=4, uniform='title')
        frame.columnconfigure(3, weight=1, uniform='title')
        frame.rowconfigure(0, weight=1)

        # Define and place the widgets
        title_lbl = ttk.Label(frame, text=title, style=format)
        title_lbl.grid(column=1, row=0, sticky=tk.W)
        self.barista_lbl = ttk.Label(frame, text='Barista: Maya', style=format)
        self.barista_lbl.grid(column=2, row= 0, columnspan=2, sticky=tk.E)

        # Places frame widget
        frame.grid(column=0, row=0, pady=(5, 0), sticky=tk.NW)

        return frame

    def create_order_frame(self, parent: ttk.Frame) -> ttk.Frame:
        '''
        Description: Create frame for order entry
        Param: parent - The frame that holds the widget
        Return: frame - order frame with content
        '''

        # Create frame widget
        frame = ttk.LabelFrame(parent, text='  Order Information  ')
        frame.configure(borderwidth=1, relief=tk.SOLID)

        # Configure layout proportions for 
        # Order Information section frame
        frame.columnconfigure((0, 1), weight=1)
        frame.rowconfigure(0, weight=1)

        # Define and place the widgets

        #  ----- Start Item Order frame -----------------

        # Create item order Frame
        item_order_frm = ttk.Frame(frame)
        item_order_frm.grid(column=0, row=0, pady=(5, 0),
                            sticky=tk.EW)

         # Layout grid for order frame
        item_order_frm.columnconfigure(0, weight=1)
        item_order_frm.columnconfigure(1, weight=1)
        item_order_frm.rowconfigure((0, 1, 2, 3), weight=1)

        # Enter item quantity
        ttk.Label(item_order_frm,
                  text='Quantity').grid(column=0, row=0,
                                        padx=(40, 0), sticky=tk.W)
        self.quantity_ent = ttk.Entry(item_order_frm,
                                      justify=tk.RIGHT, width=10
                                      )
        self.quantity_ent.grid(column=1, row=0, padx=(0, 0), 
                               pady=(10, 0), sticky=tk.W)
        
        # Select if taxable
        self.taxable_chk = ttk.Checkbutton(item_order_frm,
                                           text='Taxable?',
                                           onvalue='1',
                                           offvalue='0')
        self.taxable_chk.grid(column=0, row=1,
                              padx=(40, 0), pady=(10, 10), sticky=tk.W)

        # Create item order buttons
        ttk.Button(item_order_frm, text='Calculate \n Selection', width=10,
                   ).grid(
            column=0, row=2, padx=(0, 10), pady=(0, 10), sticky=tk.E)
        self.next_item_btn = ttk.Button(
            item_order_frm, text='Clear for \n Next Item')
        self.next_item_btn.grid(column=1, row=2, padx=(
            10, 10), pady=(0, 10), sticky=tk.W)
        self.next_item_btn.config(state=tk.DISABLED)

        # Create item amount display field
        ttk.Label(item_order_frm,
                  text='Item Amount').grid(column=0, row=3,
                                           padx=(40, 10), sticky=tk.W)

        self.item_amt_ent = tk.Entry(
            item_order_frm, 
            justify=tk.RIGHT, width=10,
            borderwidth=1, state=tk.DISABLED, 
            disabledbackground='white', disabledforeground='Black')
        self.item_amt_ent.grid(column=1, row=3,  pady=(0, 1))      
        
        #  ----- End Item Order frame -----------------

        #  ----- Start Item Type frame ----------------

        # Create item type Frame
        item_type_frm = ttk.Frame(frame)
        item_type_frm.grid(column=1, row=0,  pady=(10, 30), sticky=tk.EW)


        # Layout grid for order frame
        item_type_frm.columnconfigure(0, weight=1)
        item_type_frm.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Create coffee options
        ttk.Label(item_type_frm, text='Coffee Selections').grid(
            column=0, row=0, sticky=tk.W)

        ttk.Radiobutton(item_type_frm, text='Coffee 1', value='price 2',
                        ).grid(column=0, row=1, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text='Coffee 2', value='price 2',
                        ).grid(column=0, row=2, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text='Coffee 3', value='price 2',
                        ).grid(column=0, row=3, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text='Coffee 4', value='price 2',
                        ).grid(column=0, row=4, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text='Coffee 5', value='price 2',
                        ).grid(column=0, row=5, padx=(10, 0), pady=(0, 15),
                                sticky=tk.W)

        #  ----- End Item Type frame ------------------

        # Places frame widget
        frame.grid(column=0, row=1, padx=(10, 10), pady=(15, 0), sticky=tk.EW)

        return frame

    def create_total_frame(self, parent: ttk.Frame) -> ttk.Frame:
        '''
            Description: Create frame for order totals
            Param: container - Parent grid container
            Return: frame - total frame with content
        '''

        # Create frame widget
        frame = ttk.LabelFrame(parent, text='  Order Totals  ')
        frame.config(borderwidth=1, relief=tk.SOLID)

        # Configure layout proportions for 
        # Total section frame
        # Layout grid for title frame
        frame.columnconfigure(0, weight=1, uniform='total')
        frame.columnconfigure(1, weight=2, uniform='total')
        frame.columnconfigure(2, weight=4, uniform='total')
        frame.rowconfigure((0, 1, 2), weight=1)

        # Create summary labels
        ttk.Label(frame, text='Sub Total').grid(column=1, row=0, sticky=tk.W)
        ttk.Label(frame, text='Tax').grid(column=1, row=1, sticky=tk.W)
        ttk.Label(frame, text='Total Due').grid(column=1, row=2, sticky=tk.W)
        
        # Create summary fields
        self.sub_total_ent = tk.Entry(frame,
            width=10, justify=tk.RIGHT, state=tk.DISABLED, 
            disabledbackground='white', disabledforeground='Black')
        self.sub_total_ent.grid(column=2, row=0, pady=(5, 0), sticky=tk.W)

        self.sub_tax_ent = tk.Entry(frame, 
            width=10, justify=tk.RIGHT, state=tk.DISABLED, 
            disabledbackground='white', disabledforeground='Black')
        self.sub_tax_ent.grid(column=2, row=1, pady=(5, 0), sticky=tk.W,)
        
        self.total_due_ent = tk.Entry(frame, 
            width=10, justify=tk.RIGHT, state=tk.DISABLED, 
            disabledbackground='white', disabledforeground='Black')
        self.total_due_ent.grid(column=2, row=2, pady=(5, 10), sticky=tk.W)

        # Places frame widget
        frame.grid(column=0, row=2, padx=(10, 10), pady=(10, 10), sticky=tk.EW)

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

        self.COFFEE_DB = 'coffee_shoppe/coffee.db'
        self.LOGIN_DB = 'coffee_shoppe/login.db'

        self.style = ttk.Style(self)
        self.TITLE_FONT = ('Sans', 12, "bold")

        # Track login and page display
        self.logged_in = False

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
        # page_menu.add_command(label='Page 1', command=lambda: self.show_frame('Page1'))
        if self.logged_in:
            page_menu.add_command(
                label='Log out', command=lambda: self.frames['Page2'].logout())
            page_menu.add_command(
                label='Page 3', command=lambda: self.show_frame('Page3'))
        else:
            page_menu.add_command(
                label='Login', command=lambda: self.show_frame('Page2'))


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
