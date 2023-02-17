"""
Program: blog_8
Creation Data: 02/15/2023
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Creating a Class-based Python Tkinter Template - Part 8

Description: Post part of a series on creating a class-based GUI
            using Python's Tkinter module.

Previous code: blog_7 available on github

Changes: 02/15/2023 - Access data/functions on different pages. 
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

        # Answer to the question
        self.pg2_answer = 'African or European?'

        #  ====== Optional ========
        # self.score = ''

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
        ##  ====== Optional ========
        # self.set_row_proportions(frame, (1, 1))

        # Create and place two Label widgets
        title_lbl = tk.Label(frame, text = '-- Page 1 --', font=self.TITLE_FONT)
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)
        page_btn = ttk.Button(frame, text = 'Page 2', width = 10,
            command=lambda: self.ctrl.show_frame('Page2') )
        page_btn.grid(column = 0, row = 2,pady=(30, 20), sticky = tk.N)
        ##  ====== Optional ========
        # self.score_lbl = tk.Label(frame, text = f'Number Correct: ')
        # self.score_lbl.grid(column = 0, row = 1, pady=(5, 0), sticky = tk.EW)

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

    #  ====== Optional ========
    # def update_score(self) -> None:
    #     """
    #     Description: Updates the display with the number of correct
    #                  answers from the page 2 question
    #     Returns: None
    #     """
    #     self.score_lbl.configure(text=f'Number Correct: {self.score}')


class Page2(tk.Frame): 
    # Container frame for page content
    def __init__(self, parent, controller):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Provide navigation and access to page data
        self.ctrl = controller
        
        #  ====== Optional ========
        # self.correct = 0

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
        frame.columnconfigure(0, weight = 1)
        self.set_row_proportions(frame, (1, 1, 1, 1, 1, 1, 1))

        # Create and place two Label widgets
        title_lbl = tk.Label(frame, text = '-- Page 2 --', font=self.TITLE_FONT)
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)
        self.question_lbl = tk.Label(frame, 
            text='What is the airspeed velocity \nof an unladen swallow?')
        self.question_lbl.grid(column = 0, row = 1, pady=(10, 5), sticky = tk.EW)
        self.question_ent = ttk.Entry(frame, width=20)
        self.question_ent.grid(column = 0, row = 2, pady=(10, 5), sticky = tk.N)
        self.answered_lbl = tk.Label(frame, text='Your Answer: ')
        self.answered_lbl.grid(column = 0, row = 3, padx=(30, 0), pady=(5, 5), sticky = tk.W)
        self.answer_lbl = tk.Label(frame, text='Correct Answer: ')
        self.answer_lbl.grid(column = 0, row = 4, padx=(30, 0), pady=(5, 5), sticky = tk.W)
        answer_btn = ttk.Button(frame, text = 'Answer', width = 10,
            command=self.show_answer)
        answer_btn.grid(column = 0, row = 5, pady=(10, 5), sticky = tk.N)
        page_btn = ttk.Button(frame, text = 'Page 1', width = 10,
            command=lambda: self.ctrl.show_frame('Page1') )
        page_btn.grid(column = 0, row = 6, pady=(5, 10), sticky = tk.N)

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

    def show_answer(self) -> None:
        """
        Description: Display the entered and correct answers. 
                     Optionally: Updates number of correct 
                     displayed on page 1.
        Returns: None
        """
        # Gets correct answer from page 1
        b_of_d_answer = self.ctrl.frames['Page1'].pg2_answer
        # Gets entered answer
        answered = self.question_ent.get()
        # Displays correct and entered answer
        self.answer_lbl.configure(text=f'Correct Answer: {b_of_d_answer}')
        self.answered_lbl.configure(text=f'Your Answer: {answered}')

        #  ====== Optional ========
        # # Check if entered answer is the same as correct one
        # if answered.lower() == b_of_d_answer.lower():
        #     # Increase correct count
        #     self.correct += 1
        # # Assign correct count to score on page 1
        # self.ctrl.frames['Page1'].score = self.correct
        # # Call page 1 method to update score displayed on page 1
        # self.ctrl.frames['Page1'].update_score()


class App(tk.Tk):  
    # Inheriting from Tk class
    def __init__(self):
        super().__init__()  
        # Update tuple with Page classes to be 
        # added to frames dictionary
        self.PAGES = (Page1, Page2)  

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
        self.iconbitmap(self, default='./wolftrack.ico')
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
