"""
Program: Main 4
Creation Data: 08/206/2023
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: 

Description: Post part of a series on creating a point of sales system
            using Python's Tkinter module. 

            - Blog 16 Create Coffee table in coffee.db 
            - Blog 16 Create layout for Order Entry page
            - Blog 17 Update menu bar
            - Blog 17 Add transition to Order Entry page on successful log in
            - Blog 17 Update coffee type info with data from coffee database
            - Blog 18 Add class variables and vars
            - Blog 18 Add ability to or multiple coffee types in an order
            - Blog 18 Calculate order summary (subtotal, tax, and total due)

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
            # self.instructions_lbl.configure(text=f'{self.emp_name} is successfully login')

            # Set to update menu bar 
            self.ctrl.logged_in = True
            self.ctrl.create_menu_bar(self.ctrl)
            self.clear_login_entries()

            # Update barista name on Order Entry and employee id on Payment pages
            self.ctrl.frames['Page3'].barista_name = self.emp_name

            # Update the label text on Order Entry to show employee's name
            self.ctrl.frames['Page3'].barista_lbl.configure(text=f"Barista: {self.ctrl.frames['Page3'].barista_name}")

            self.ctrl.show_frame('Page3')
            
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

        # Constraints
        self.DATABASE = self.ctrl.COFFEE_DB
        self.COFFEE_OPTIONS = self.get_coffee_info()
        self.TAX_RATE = 0.06

        # Configure style
        self.ctrl.style.configure('Title.TLabel', 
                             font=(self.ctrl.TITLE_FONT))
        
        # Initialize variables
        self.barista_name = ''                  # Name of barista placing order
        self.quantity = 0                       # Number of specific item
        self.index_offset = 1                   # Offset item id to match position in list
        self.subtotal = 0                       # Subtotal of order
        self.tax = 0                            # Tax on order
        self.total_due = 0                      # Total cost of order
        self.order_date = ''                    # Date order was created
        self.order_time = ''                    # Time order was created
        self.order_items = []                   # Info on items ordered
        self.order = []                         # Info on individual order
        self.orders = []                        # List of all orders

        self.item_type_int = tk.IntVar()
        self.quantity_ent_str = tk.StringVar(value='')
        self.item_amt_ent_str = tk.StringVar(value='')
        self.taxable_chk_str = tk.StringVar(value='1')  # Default is taxable
        self.item_amt_str = tk.StringVar(value='')
        self.item_type_str = tk.StringVar(value='')
        self.subtotal_str = tk.StringVar(value='')
        self.tax_str = tk.StringVar(value='')
        self.total_due_str = tk.StringVar(value='')


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
                                      textvariable=self.quantity_ent_str,
                                      justify=tk.RIGHT, width=10)
        self.quantity_ent.grid(column=1, row=0, padx=(0, 0), 
                               pady=(10, 0), sticky=tk.W)
        
        # Select if taxable
        self.taxable_chk = ttk.Checkbutton(item_order_frm,
                                           text='Taxable?',
                                           variable=self.taxable_chk_str,
                                           onvalue='1',
                                           offvalue='0')
        self.taxable_chk.grid(column=0, row=1,
                              padx=(40, 0), pady=(10, 10), sticky=tk.W)

        # Create item order buttons
        ttk.Button(item_order_frm, text='Calculate \n Selection', width=10,
                  command=self.cal_item_amt).grid(
            column=0, row=2, padx=(0, 10), pady=(0, 10), sticky=tk.E)
        self.next_item_btn = ttk.Button(item_order_frm, 
                                         text='Clear for \n Next Item',
                                         command=self.next_item)
        self.next_item_btn.grid(column=1, row=2, padx=(
            10, 10), pady=(0, 10), sticky=tk.W)
        self.next_item_btn.config(state=tk.DISABLED)

        # Create item amount display field
        ttk.Label(item_order_frm,
                  text='Item Amount').grid(column=0, row=3,
                                           padx=(40, 10), sticky=tk.W)

        self.item_amt_ent = tk.Entry(
            item_order_frm, textvariable=self.item_amt_ent_str,
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

        ttk.Radiobutton(item_type_frm, text=self.COFFEE_OPTIONS[0][1], 
                                       value=self.COFFEE_OPTIONS[0][0],
                                       variable=self.item_type_int
                        ).grid(column=0, row=1, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text=self.COFFEE_OPTIONS[1][1], 
                                       value=self.COFFEE_OPTIONS[1][0],
                                       variable=self.item_type_int
                        ).grid(column=0, row=2, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text=self.COFFEE_OPTIONS[2][1], 
                                       value=self.COFFEE_OPTIONS[2][0],
                                       variable=self.item_type_int
                        ).grid(column=0, row=3, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text=self.COFFEE_OPTIONS[3][1], 
                                       value=self.COFFEE_OPTIONS[3][0],
                                       variable=self.item_type_int
                        ).grid(column=0, row=4, padx=(10, 0), sticky=tk.W)
        ttk.Radiobutton(item_type_frm, text=self.COFFEE_OPTIONS[4][1], 
                                       value=self.COFFEE_OPTIONS[4][0],
                                       variable=self.item_type_int
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
        self.sub_total_ent = tk.Entry(frame, textvariable=self.subtotal_str,
            width=10, justify=tk.RIGHT, state=tk.DISABLED, 
            disabledbackground='white', disabledforeground='Black')
        self.sub_total_ent.grid(column=2, row=0, pady=(5, 0), sticky=tk.W)

        self.sub_tax_ent = tk.Entry(frame, textvariable=self.tax_str,
            width=10, justify=tk.RIGHT, state=tk.DISABLED, 
            disabledbackground='white', disabledforeground='Black')
        self.sub_tax_ent.grid(column=2, row=1, pady=(5, 0), sticky=tk.W,)
        
        self.total_due_ent = tk.Entry(frame, textvariable=self.total_due_str,
            width=10, justify=tk.RIGHT, state=tk.DISABLED, 
            disabledbackground='white', disabledforeground='Black')
        self.total_due_ent.grid(column=2, row=2, pady=(5, 10), sticky=tk.W)

        # Places frame widget
        frame.grid(column=0, row=2, padx=(10, 10), pady=(10, 10), sticky=tk.EW)

        return frame

    def get_coffee_info(self) -> list[tuple]:
        """
        Description: Gets the coffee types and costs from Coffees table 
                    in coffee db supplied in login page
        Param: None
        Returns      The coffee info
        """
        coffee_sql = 'SELECT * FROM Coffees'
        conn = dbu.create_connection(self.DATABASE)
        results = dbu.get_all_records(conn, coffee_sql, self.DATABASE)
        return results

    def get_item_cost(self) -> float:
        '''
        Description: Gets unit cost of selected item
        Param: None
        Return: Unit cost
        '''     
        selected = self.item_type_int.get() - self.index_offset
        return self.COFFEE_OPTIONS[selected][2]    

    def cal_item_amt(self) -> None:
        '''
        Description: Calculates selected item amount
        Param: none
        Return: None
        '''
        self.quantity = int(self.quantity_ent_str.get())
        self.coffee_type = self.item_type_int.get() - self.index_offset

        if self.quantity > 0 and self.item_type_int.get() != None:
            item_amt = round(self.quantity
                                * self.get_item_cost(), 2)
            self.subtotal += item_amt           
            self.item_amt_ent_str.set(f'{item_amt: .2f}')

            self.order_items.append((self.quantity, self.coffee_type,
                                        self.get_item_cost(), item_amt))           
            print(self.order_items)

            self.next_item_btn.config(state=tk.NORMAL)

    def get_tax(self) -> float:
        '''
        Description: Calculates tax on taxable orders
        Param: none
        Return: tax on order
        '''
        if self.taxable_chk_str.get():
            return float(self.subtotal) * self.TAX_RATE
        else:
            return 0.00

    def summary(self) -> None:
        '''
        Description: Tallies order and adds tax if taxable
        Param: ctrl - Reference the App class
        Return: None
        '''
        # Calculate tax and payment
        self.tax = self.get_tax()
        self.total_due = self.subtotal + self.tax

        # tally number of items in order
        # num_of_items = self.get_num_of_items(self.order_items)

        # Display in summary fields
        self.subtotal_str.set(f'{self.subtotal: .2f}')
        self.tax_str.set(f'{self.tax: .2f}')
        self.total_due_str.set(f'{self.total_due: .2f}')

    def clear_order_entries(self) -> None:
        '''
        Description: Clears order entry fields
        Param: none
        Return: None
        '''
        self.quantity_ent.delete(0, tk.END)
        self.item_amt_ent.configure(state=tk.NORMAL)
        self.item_amt_ent.delete(0, tk.END)
        self.item_amt_ent.configure(state=tk.DISABLED)

    def reset_order_entry_vars(self) -> None:
        '''
        Description: Resets order entry field variables
        Param: none
        Return: None
        '''
        self.quantity_ent_str.set('')
        self.item_amt_str.set('')
        self.item_type_int.set(None)

    def next_item(self) -> None:
        '''
        Description: Clears order entry fields and vars
        Param: none
        Return: None
        '''        
        self.reset_order_entry_vars()
        self.clear_order_entries()

    def new_order(self, ctrl) -> None:
        pass


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
        if self.logged_in:
            page_menu.add_command(
                label='Log out', command=lambda: self.frames['Page2'].logout())
            page_menu.add_command(
                label='Order Entry', command=lambda: self.show_frame('Page3'))
        else:
            page_menu.add_command(
                label='Login', command=lambda: self.show_frame('Page2'))


        # Create Exit menu item
        page_menu.add_separator()
        page_menu.add_command(label='Exit', command=self.quit)

        # Add Pages menu and menu items to the menu bar
        self.menu_bar.add_cascade(label='Pages', menu=page_menu)

        # Create options for Task menu
        if self.logged_in:
            self.tasks_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.create_tasks2menu()
            self.menu_bar.add_cascade(label='Tasks', menu=self.tasks_menu)

        # Create options for Help menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)

        # Create Help menu item and add menu and menu item to menu bar
        help_menu.add_command(label='Help', command=self.help)
        self.menu_bar.add_cascade(label='Help', menu=help_menu)

        # Assign menu bar to the window
        self.config(menu=self.menu_bar)

    def create_tasks2menu(self) -> None:  # Order Entry
        self.tasks_menu.delete(0, 'end')  
        self.tasks_menu.add_command(label='Calculate Item', 
                                    command=lambda: self.frames['Page3'].cal_item_amt())
        self.tasks_menu.add_command(label='Next Item',
                                    command=lambda: self.frames['Page3'].next_item())
        self.tasks_menu.add_separator()
        self.tasks_menu.add_command(label='Calculate Total',
                                    command=lambda: self.frames['Page3'].summary())
        self.tasks_menu.add_command(label='New Order', 
                                    command=lambda: self.frames['Page3'].new_order(self))

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
