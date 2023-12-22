"""
Program: blog_7a
Creation Data: 01/25/2023
Revision Date: 11/13/2923
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Creating a Class-based Python Tkinter Template - Part 7

Description: Post part of a series on creating a class-based GUI
            using Python's Tkinter module.

Previous code: blog_6 available on github

Changes: 01/25/2023 - Added menu bar with navigation options. 
Changes: 04/29/2023 - Update path to favicon after move to templates folder
Changes: 11/13/2923 - Added PageFrame and PageTitle classes to generate pages
""" 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PageContent(tk.LabelFrame):
    """
    Description: Label frame for page content
    Param: parent - Container widget (App class) into which page frame is placed
    Param: controller - Reference to App class that contains the pages
    """
    def __init__(self, parent, lbl_frm_title, frm_border):
        super().__init__(parent, text=lbl_frm_title, borderwidth=frm_border)

        # Places instance in parent
        self.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)


class PageTitle(ttk.Label):
    """
    Description: Creates page title
    Param: parent - Container widget into which frame is placed
    Param: text - Title text
    Param: style - Style for title text
    """
    def __init__(self, parent, title, style):
        super().__init__(parent, text=title, style=style)

        # Places instance in parent
        self.pack(side=tk.TOP, pady=(20, 0))


class PageFrame(ttk.Frame):
    """
    Description: Base page frame for creating app pages
    Param: parent - Container widget (App class) into which page frame is placed
    Param: controller - Reference to App class that contains the pages
    """
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.ctrl = controller
        self.page_title = ''
        self.next_page = ''
        
        # Configure style
        self.style = ttk.Style(self)
        self.style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the the labelFrame widget
        self.page_content_frm = PageContent(self, 'Screen Frame', 1)

        # Create the content for the labelFrame widget
        self.create_page_content(parent=self.page_content_frm)

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_page_content(self, parent:tk.Frame) -> None:
        """
        Description: Creates page title and navigation button
        Param: parent  - Container widget into which frame is placed
        Return: None
        """
        # Create and place Label widgets
        self.title_lbl = PageTitle(parent, 
                                   self.page_title, 
                                   'Title.TLabel')
        self.title_lbl.pack(side=tk.TOP, pady=(20, 0))
        self.page_btn = ttk.Button(parent, text = f'Page {self.next_page}', width = 10,
                              command=lambda: self.ctrl.show_frame(f'Page{self.next_page}'))
        self.page_btn.pack(side=tk.TOP, expand=True)


class Page1(PageFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Define values for content widgets
        self.page_title = '-- Page 1 --'
        self.btn_text = 'Button 2'
        self.next_page = '2'

        # Set values for content widget
        # These will overwrite the empty string values in 
        # the PageFrame class        
        self.title_lbl.configure(text=self.page_title)
        self.page_btn.configure(text=self.btn_text)


class Page2(PageFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Define values for content widgets
        self.page_title = '-- Page 2 --'
        self.btn_text = 'Button 3'
        self.next_page = '3'

        # Set values for content widget
        self.title_lbl.configure(text=self.page_title)
        self.page_btn.configure(text=self.btn_text)


class Page3(PageFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Define values for content widgets
        self.page_title = '-- Page 3 --'

        # Set values for content widget
        self.title_lbl.configure(text=self.page_title)


    def create_page_content(self, parent:tk.Frame) -> None:
        """
        Description: Creates page title and navigation button
        Param: parent  - Container widget into which frame is placed
        Return: None
        """
        # Create and place Label widgets
        self.title_lbl = PageTitle(parent, 
                                   self.page_title, 
                                   'Title.TLabel')
        self.title_lbl.pack(side=tk.TOP, pady=(20, 0))

        self.pages = ['1', '2']
        self.page_var = tk.StringVar(value=self.pages[0])
        self.page_nav_cmb = ttk.Combobox(parent, 
                                    textvariable=self.page_var)
        self.page_nav_cmb.set('Select Page Number')
        self.page_nav_cmb['values'] = self.pages # first item not initially shown
        self.page_nav_cmb.pack(side=tk.TOP, expand=True)

        # # Program events
        self.page_nav_cmb.bind('<<ComboboxSelected>>', 
                        lambda event: self.page_selection(self.page_var.get()))

    def page_nav_reset(self):
        self.pages_var = tk.StringVar(value=self.pages[1])
        self.page_nav_cmb.set('Select Page Number')
        self.page_nav_cmb['values'] = self.pages

    def page_selection(self, value:str) -> None:
        self.ctrl.show_frame(f'Page{value}')
        self.page_nav_reset()
        self.focus()
       

class App(tk.Tk):  
    # Inheriting from Tk class
    def __init__(self):
        super().__init__()  
        # Update tuple with Page classes to be 
        # added to frames dictionary
        self.PAGES = (Page1, Page2, Page3)  

        # Program Info
        WINDOW_WIDTH = 300
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
        # self.iconbitmap(self, default='./templates/wolftrack.ico')
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
