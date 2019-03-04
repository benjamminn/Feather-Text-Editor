'''
Author(s): Benjamin Gordon
Last Edited: 02/6/2019
Purpose: Handles all text traversal operations.
'''

# Imports
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
class TraversalClass(object):
    '''
    Handles all text manipulation functions
    '''
    
    def search(searchtext, textbox, window):
        '''
        Search naive algorithm that searches through text block and then gives coordinates to be marked in the document.
        '''
        
        # Closes current search window.
        window.destroy()
        
        # Gets block of text.
        document = textbox.get("1.0", "end-1c")
        
        # Current line
        line = 1
        
        # Place in the line
        linespace = 0
        
        # Traverses document with i being the beginning of the currently checked place.
        for i in range((len(document)-len(searchtext)) + 1):
            
            # Increments j to be at the end of the checked space
            j = i + len(searchtext)
            
            # Checks the string from i to j
            if document[i:j] == searchtext:
               
               # Assembles beginning coordinates
               beg = str(line) + '.' + str(i - linespace)
               
               # Assembles ending coordinates
               end = str(line) + '.' + str((j - linespace))
               
               # Select between the space between the two coordinates in the text3
               textbox.tag_add(SEL, beg, end)
               
            # Handles incrementation for a newline.
            if document[i:i+1] == '\n':
               line += 1
               linespace = i + 1
            
            
    def replace(searchtext, replacetext, textbox, window):
        '''
        Replace naive algorithm that searches through text block and then gives coordinates to be marked in the document.
        '''
        
        # Closes current replace window.
        window.destroy()
        
        # # Gets document
        document = textbox.get("1.0", "end-1c")
        
        # Current line
        line = 1
        
        # Place in the line.
        linespace = 0
        
        # Traverses document with i being the beginning of the currently checked place.
        for i in range((len(document)-len(searchtext)) + 1):
            
            # Increments j to be at the end of the checked space
            j = i + len(searchtext)
            
            # Checks the string from i to j
            if document[i:j] == searchtext:
               
               # Assembles beginning coordinates
               beg = str(line) + '.' + str(i - linespace)
               
               # Assembles ending coordinates
               end = str(line) + '.' + str((j - linespace))
               

               # Deletes the current word and replaces it with the desired one.
               textbox.delete(beg, end)
               textbox.insert(beg, replacetext)
               
            # Handles incrementation for a newline. 
            if document[i:i+1] == '\n':
               line += 1
               linespace = i + 1
               