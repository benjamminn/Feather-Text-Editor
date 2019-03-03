'''
Author(s): Benjamin Gordon
Last Edited: 02/6/2019
Purpose: Handles all program operations.
'''

# Imports
from clipboard import ClipboardClass
from windows import WindowsClass
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter.ttk import Button


class ProgramFunctionsClass(object):
    '''
    Handles all program functions.
    '''


    def __init__(self, mainwindow, textbox):
        '''
        Constructor
        '''
        
        # The text editor window
        self.mainwindow = mainwindow
        
        # Textbox object.
        self.textbox = textbox
        
        # The clipboard manipulation class.
        self.clipboard = ClipboardClass
        
        # Current text being taken from or put in on the clipboard.
        self.text = ''
        


    def copy(self):
        '''
        Copies selected text from editor to clipboard.
        '''
        try:
       
             # Gets selected text from the editor
            self.text = self.textbox.get("sel.first", "sel.last")
            
            # Puts the text in the clipboard
            self.clipboard.inputwindowsclipboard(self.text)
        
        except: 
        
              return
        
        
    def cut(self):
        '''
       Moves selected text from editor to clipboard.
        '''
        
        try:
       
            # Gets selected text from the editor
            self.text = self.textbox.get("sel.first", "sel.last")
            
            # Puts the text in the clipboard.
            self.clipboard.inputwindowsclipboard(self.text)
            
            # Deletes selected text
            self.textbox.delete("sel.first", "sel.last")
        
        except: 
        
              return

    def paste(self):
        '''
        Copiess text from the clipboard into the textbox.
        '''
        
        # Gets selected text from clipboard.
        self.text = self.clipboard.outputwindowsclipboard()

        # Inserts text into the textbox.
        self.textbox.insert('insert', self.text)
        

               
    def dosearch(self):
        '''
        Searches the document for the ones the user specifies.
        '''
        
        # Call the search window.
        WindowsClass.searchbox(self.mainwindow, self.textbox)
        
 
    def doreplace(self):
        
        # Call the replace window.
        WindowsClass.replacebox(self.mainwindow, self.textbox)

    

    
    def mousemenu(self, place):
        
        mousemenu = Menu(self.mainwindow, tearoff=0) 
        
        mousemenu.add_command(label = 'Cut', command=lambda: self.cut())
    
        mousemenu.add_command(label = 'Copy', command=lambda: self.copy())
      
        mousemenu.add_command(label = 'Paste', command=lambda: self.paste())  
        
        mousemenu.post(place.x_root, place.y_root)     
    
    def quit(self):
        '''
        Quits Application
        '''
        
        # Opens close window.
        WindowsClass.onclose(self.mainwindow)
    

        
    
        
        