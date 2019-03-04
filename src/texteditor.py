'''
Author(s): Benjamin Gordon
Last Edited: 02/06/2019
Purpose:  Creates main window.
'''  

# Imports
import tkinter
from tkinter.ttk import Button
from tkinter import Menu
from filefunctions import FileFunctionsClass
from programfunctions import ProgramFunctionsClass
from windows import WindowsClass
from smtpd import program



class TextEditorClass:
    
        def create():
            '''
            Creates the initial window, textbox and menus.
            '''
           
            # Creates main window
            mainwindow = tkinter.Tk() 
            
            # Set Pixel Size
            mainwindow.geometry("1000x500")
            

            
            # Sets Title
            mainwindow.title('Feather Text Editor')
                
            # Creates textbox.    
            textbox = tkinter.Text(mainwindow)
            
        
            # Dropdown menu
            dropdown = Menu(mainwindow)
            
            # Attaches dropdown menu to mainwindow.
            mainwindow.config(menu = dropdown)  
            
            # Creates scroll object.
            scroll = tkinter.Scrollbar(textbox, command=textbox.yview)
            
            # Attaches scrollbar and main menu to mainmenu.
            textbox.pack(side="left", fill="both", expand=1)
            scroll.pack(side="right", fill="y")
            
            # Tkinter scroll attribute.
            textbox.configure(yscrollcommand=scroll.set)
            
            # File menu object.
            filedropdown = Menu(dropdown, tearoff=0)
            
            # Edit menu object.
            editdropdown = Menu(dropdown, tearoff=0)
            
            # Help menu object.
            helpdropdown = Menu(dropdown, tearoff=0)
            
            # Adds menus objects to dropdown menu.
            dropdown.add_cascade(label = 'File', menu = filedropdown)
            dropdown.add_cascade(label = 'Edit', menu = editdropdown)
            dropdown.add_cascade(label = 'Help', menu = helpdropdown)
        
            # Creates filefunctions and programfunction object.
            filefunctions = FileFunctionsClass(mainwindow, textbox)
            programfunctions = ProgramFunctionsClass(mainwindow, textbox)
            
            # Right click for Mousemenu.
            textbox.bind("<Button-3>", programfunctions.mousemenu)
            
            # File drop down menu commands.
            filedropdown.add_command(label = 'New', command=lambda: filefunctions.new())
            
            filedropdown.add_command(label = 'Open', command=lambda: filefunctions.open())
            
            filedropdown.add_command(label = 'Save', command=lambda: filefunctions.save())
            
            filedropdown.add_command(label = 'Save As' , command=lambda: filefunctions.saveas())
            
            filedropdown.add_separator()
            
            filedropdown.add_command(label = 'Quit' , command=lambda: programfunctions.quit())
            
            
            # Edit dropdown menu commands.           
            editdropdown.add_command(label = 'Cut', command=lambda: programfunctions.cut())
            
            editdropdown.add_command(label = 'Copy', command=lambda: programfunctions.copy())
            
            editdropdown.add_command(label = 'Paste', command=lambda: programfunctions.paste())
            
            editdropdown.add_separator()
            
            editdropdown.add_command(label = 'Search', command=lambda: programfunctions.dosearch())  
            
            editdropdown.add_command(label = 'Replace', command=lambda: programfunctions.doreplace()) 
            
            # Help dropdown menu commands.    
            helpdropdown.add_command(label = 'About', command=lambda:WindowsClass.about(mainwindow)) 
            
            # Windows exit messagebox
            mainwindow.protocol("WM_DELETE_WINDOW", lambda:programfunctions.quit())
            
            # Starts GUI loop.
            mainwindow.mainloop()