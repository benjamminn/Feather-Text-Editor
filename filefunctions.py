'''
Author(s): Benjamin Gordon
Last Edited: 02/6/2019
Purpose: Handles all file operations.
'''
# Imports
import tkinter  
from tkinter.filedialog import asksaveasfilename, askopenfilename
from windows import WindowsClass
from tkinter import Menu


class FileFunctionsClass(object):
    '''
    Gives functionality to buttons in the editor.
    '''

    def __init__(self, mainwindow, textbox):
        '''
        Constructor
        '''
        
        # Global filepath.
        self.filepath = ''
        
        # Text editor window
        self.mainwindow = mainwindow
        
        # Main textbox.
        self.textbox = textbox
        
        
        
    def new(self):
        """
        Clears textbox.
        """
        
        # Deletes letters in textbox.
        self.textbox.delete(1.0, "end")
        
        
    def open(self):
        '''
        Opens and loads a new file.
        '''
        try:
       
            # Ask for file name thats being opened. 
            self.filepath = askopenfilename()
            
            # File pointer
            fp = open(self.filepath, encoding = 'utf-8')
            
            # Gets save location.
            savetext = fp.read()
            
            # Clears the textbox
            self.textbox.delete(1.0, "end")
            
            # Fills the textbox
            self.textbox.insert(1.0, savetext)    
        
        
        except: 
        
              return
        

        
        
    def save(self):
        '''
        Saves document to current path.
        '''
        
        # Creates warning and doesn't save if it has not been saved to a location or opened from a location. 
        if self.filepath == '':
            
           # Error message for no location.
           Messagewindows.popup('Error', 'No file location found.')
           

        else:
            
            # Get text 
            savetext = self.textbox.get("1.0", "end-1c")   

             # Creates pointer to filepath
            fp = open(self.filepath, 'w')
        
            # Writes to file
            fp.write(savetext)
        
            # Closes file connection
            fp.close()         
    
        
    def saveas(self):
        '''
        Saves document to user specified path.
        '''
        
        try:
       
            # Gets text
            savetext = self.textbox.get("1.0", "end-1c") 
            
            # Gets file path from menu.
            self.filepath = asksaveasfilename(defaultextension=".txt", initialfile='textdocument.txt', filetypes=[("All Files","*.*"), ("Text File","*.txt")]) 
            
            # Creates pointer to filepath.
            fp = open(self.filepath, 'w')
            
            # Writes text to filepath.
            fp.write(savetext)
            
            # Closes file connection.
            fp.close()         
        
        
        except: 
        
              return
        

    