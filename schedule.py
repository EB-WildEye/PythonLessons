# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Schedule ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" create a schedule for a class """
import tkinter as tk
from tkinter import *


def main():

    app = tk.Tk()  # create a new window
    app.geometry("940x700") # set the window's size
    app.title("Schedule")
    app.maxsize(940,700)
    app.minsize(940,700)


    """ create a table for week days on the xaixs at the top of the window """

    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for i in range(7):
        day = Label(app,text=week_days[i],width=18, height=6, borderwidth=3,relief=RIDGE)
        day.grid(row=0,column=i)


    """ create a table for hours on the yaixs at the left of the window """

    hours = ["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"]

    for i in range(len(hours)):
        hour = Label(app,text=hours[i],width=18, height=3, borderwidth=3,relief=RIDGE)
        hour.grid(row=i+1,column=0)


    """ create a table for the schedule """

    for i in range(12):
        for j in range(7):
            schedule = Label(app,text="",width=18, height=3, borderwidth=3,relief=RIDGE)
            schedule.grid(row=i+1,column=j+1)

    app.mainloop()


main()