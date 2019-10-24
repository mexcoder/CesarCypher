try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu
from tkinter import *

#!/usr/bin/python
# File: toplevelminimal.py
import os
try:
    import tkinter as tk
except:
    import Tkinter as tk
import pygubu


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


class MyApplication:
    def __init__(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file(os.path.join(CURRENT_DIR, 'main.ui'))
        
        #3: Create the toplevel widget.
        self.mainwindow = builder.get_object('mainwindow')

        #4: Connect Callbacks
        builder.connect_callbacks(self)

        self.input = ""
        self.displacement = 0
        self.SpinboxChanged()

    def quit(self, event=None):
        self.mainwindow.quit()

    def run(self):
        self.mainwindow.mainloop()

    def inputChanged(self, action, value):
        self.input = value.lower()
        print("inputChanged")
        print(value)
        #self.builder.tkvariables["cesar_entry"].set(self.input)
        self.setOutput()
        return True

    def SpinboxChanged(self):
        self.displacement = self.builder.tkvariables["cesar_displacement"].get()
        self.setOutput()
    
    def setOutput(self):
        self.builder.tkvariables["cesar_output"].set(caesar(self.input, self.displacement))


caesar_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
passthrough = [" ", "ñ"]
def caesar(text, displacement):
    output = ""
    for letter in text:
        if letter in passthrough:
            output += letter
        else:
            try:
                index = caesar_alphabet.index(letter)
                index += displacement 
                output += caesar_alphabet[index % len(caesar_alphabet)] 
            except Exception as e:
                print ("Could not find character ind alphabet,", e)

    return output


if __name__ == '__main__':
    app = MyApplication()
    app.run()

# class Application:
#     def __init__(self, master):

#         #1: Create a builder
#         self.builder = builder = pygubu.Builder()

#         #2: Load an ui file
#         builder.add_from_file('main.ui')

#         #3: Create the widget using a master as parent
#         self.mainwindow = builder.get_object('Toplevel_1', master)

#         builder.connect_callbacks(self)

#     def button1_callback(self):
#         "Display the values of the 3 x Entry widget variables"
#         print(self.builder.tkvariables['entry1_var'].get())
#         print(self.builder.tkvariables['entry2_var'].get())
#         print(self.builder.tkvariables['entry3_var'].get())

#         # Change Entry_3 from green to red 
#         self.builder.tkvariables['entry3_var'].set("red")

# root = tk.Tk()
# app = Application(root)

# #print(app.mainwindow.getvar('text_1')) <-- This is commented out   
# root.mainloop()