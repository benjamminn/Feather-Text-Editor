'''
Author(s): Benjamin Gordon
Last Edited: 02/6/2019
Purpose: Handles all clipboard operations
'''
# Imports 
import subprocess
import tkinter

# Imports
class ClipboardClass(object):
    '''
    Controls clipboard operations.
    '''

                
    
    def inputwindowsclipboard(text):
        '''
        Puts input into the windows clipboard using windows 'clip' program.
        '''
        
        # Opens pipe to windows 'clip' program.
        clipboardpipe = subprocess.Popen(['clip'], stdin=subprocess.PIPE)
        
        # Sends text to 'clip' through pipe.
        clipboardpipe.communicate(input = text.strip().encode('utf-8'))  
        
        # Closes pipe.
        clipboardpipe.kill()  
        
    
    def outputwindowsclipboard():
        '''
        Returns whats in the clipboard.
        '''
        
        # Creates clipboard object.
        temp = tkinter.Tk()
        
        # Puts clipboard in withdraw mode.
        temp.withdraw()
         
        # Gets string from clipboard.
        string = temp.clipboard_get()  
    
        # Returns String
        return string  
        
 #   def Receivewindowsclipboard(self): 