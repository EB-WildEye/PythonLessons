import tkinter as tk

# ~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~

""" Let's talk about functions, why do we need them at all ? 
    Well, we can use functions to make our code more readable,
    more efficient and more reusable.
    with functions we can use the same commands as many times as we want,
    by calling the function instead of writing the same code over and over again.
    Let's start with a simple examples :

"""

#Examples:

# add() function gets 2 integar arguments and returns the sum of them
def add(x, y):
    return x + y # return statement is used to return a value from a function


# hello() function gets a string argument and print hello message
def hello(name):
    print("Hello, {}!\nLet's code together ;)".format(name)) # format() method is used to format a string
    # in this function we dont use a return statement, so the function will return None but print() function
    # will print a message to the console

# create_window() function gets a string argument and create a window with the given title

def create_window(title, message="Hello World!"):
    window = tk.Tk()
    window.title(title)
    window.geometry('500x100')
    window.resizable(0,0)
    window.configure(bg = 'purple')
    tk.Label(window, text = "{}".format(message), bg = 'black', fg = 'purple', font=("Grinched", 40) ).pack()
    tk.mainloop()
    return window



# main() function is the entry point of our program
def main():
    # call add() function and store the result in a variable
    sum = add(2, 3)
    print("Sum of 2 and 3 is : {}".format(sum))

    # call hello() function
    hello("Ahmed")

    # call create_window() function
    window = create_window(title="Hello Window", message="Hey There !")

main()