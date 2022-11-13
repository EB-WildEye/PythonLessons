# ~~~~~~~~~~~ Libraries ~~~~~~~~~~~
""" we can you code from other people to make our lives easier, it's called libraries.
    we can use libraries to do things like make a random number, or painting with turtle.
    we can also use libraries to make our own games, like Tkinter, or pygame.
    if we want to use libraries, we have to import them first. 
    you can see below that we imported the Tkinter library, and we can use it to make a window. """
from tkinter import *


# ~~~~~~~~~~~ Window ~~~~~~~~~~~

# we can make a window with Tkinter, you can see bellow how.
"""
window = Tk()
window.mainloop()
"""
# we can write things in the window,change the size, font or color etc... you can see bellow how.

root = Tk()
root.geometry("600x600") # size of the window

# To add text in the window, we use the Label function.
myLabel = Label(text=" You are the best class ever !! ", fg = "#89F96D", bg = "black", font = "Helvetica 24 bold italic", width = 20, height =7)
myLabel.pack() # this is how we add the text to the window.
root.mainloop()


# try it yourself, make a window with your name in it, and change the color, font, size etc... if you want to challenge yourself, try to search some cool fonts on google.
