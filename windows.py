'''
Author(s): Benjamin Gordon
Last Edited: 02/6/2019
Purpose: Handles all window operations.
'''
# Imports
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter.ttk import Button
from traversal import TraversalClass



class WindowsClass(object):
    '''
    Controls everything window related
    '''

    def __init__(self, mainwindow):
        '''
        Constructor
        '''
        
        self.mainwindow = mainwindow
        
        
    def popup(title, message):
        '''
        Customizable Popup Box.
        '''
        
        messagebox.showinfo(title, message)
        
        
    def searchbox(mainwindow, textbox):
        '''
        Popup box controls the search algorithm
        '''
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('Search')
        window.resizable(0, 0)
        
        # Top frame for text and entry box
        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)
        
        # Label for searchbox
        label1 = Label(frame1, text="Search for:")
        label1.pack(side = LEFT)
        
        # Entry box
        entry1 = Entry(frame1)
        entry1.pack(side = LEFT, padx = 4, pady = 4)

        # Search button
        button1 = Button(window, text="Search", command=lambda:TraversalClass.search(entry1.get(), textbox, window))
        button1.pack(side = RIGHT, padx = 4, pady = 4)
        
        # Cancel Button
        button2 = Button(window, text="Cancel", command=lambda: window.destroy())
        button2.pack(side = RIGHT, padx = 4, pady = 4)
        
    def replacebox(mainwindow, textbox):
        '''
        Popup box controls the replace algorithm
        '''
        # Creates windows with attributes
        window = Toplevel(mainwindow)
        window.title('Replace')
        window.resizable(0, 0)
        
        # Top frame for text and entry box
        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)
        
        # Labels
        label1 = Label(frame1, text="Replace:")
        label2 = Label(frame1, text="with")
        label1.pack(side = LEFT)
        
        # Search  and Replace function
        entry1 = Entry(frame1)
        entry1.pack(side = LEFT, padx = 4, pady = 4)
        label2.pack(side = LEFT)
        entry2 = Entry(frame1)
        entry2.pack(side = LEFT, padx = 4, pady = 4)
        
        # Replace Button
        button1 = Button(window, text="Replace", command=lambda:TraversalClass.replace(entry1.get(), entry2.get(), textbox, window))
        button1.pack(side = RIGHT, padx = 4, pady = 4)
        
        # Cancel Button
        button2 = Button(window, text="Cancel", command=lambda: window.destroy())
        button2.pack(side = RIGHT, padx = 4, pady = 4)
        
    def about(mainwindow):
        """
        Creates the about window
        """
        
        # About window options.
        window = Toplevel(mainwindow)
        window.resizable(0, 0)
        window.title('About')
        
        # Labels
        label1 = Label(window, text="Author: Benjamin Gordon")  
        label2 = Label(window, text="Github: https://github.com/benjamminn/Feather-Text-Editor")
        
        # Puts labels on top.
        label1.pack(side = TOP)
        label2.pack(side = TOP)
        
        # Creates textbox.    
        textbox = tkinter.Text(window) 
         

        
        # Creates scrollbar
        scroll = tkinter.Scrollbar(textbox, command=textbox.yview)
        
        textbox.insert('insert',  
"""Feather Text Editor: A classic lightweight text editor.
Copyright (C) 2019 Benjamin Gordon

The Feather Text Editor is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The Feather Text Editor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See theNU General
Public License for more details.

You should have received a copy of the GNU General Public License
along with the Feather Text Editor.  If not, see
 <https://www.gnu.org/licenses/>.""")
        
        
        # Disables Editing
        textbox.config(state=DISABLED)
                  
            
        # Attaches scrollbar and main menu to window.
        textbox.pack(side="left", fill="both", expand=1, padx = 6, pady = 6)
        scroll.pack(side="right", fill="y")  
        
        # Set Pixel Size
        window.geometry("625x300")
    
        
        
    def onclose(mainwindow):
        """
        Verify's the user wants to close.
        """
        
        # Opens messagebox to check if the user wants to quit.
        if messagebox.askyesno("Feather Text Editor","Are you sure you want to quit? \n Any unsaved work will be lost.") == True:
           mainwindow.destroy()
        
           
        
    def mousepopup(mainwindow, event):
        '''
        Controls the right click mouse popup menu.
        '''
        
        # Creates mouse menu
        mousemenu = Menu( mainwindow, event)
         
        # Mouse menu labels
        mousemenu.add_command(label = 'Cut', command=lambda: programfunctions.Cut())
        mousemenu.add_command(label = 'Copy', command=lambda: programfunctions.Copy())
        mousemenu.add_command(label = 'Paste', command=lambda: programfunctions.Paste())  
        
        # Puts menu at mouse's postion.
        mousemenu.post(place.x, place.y)
        