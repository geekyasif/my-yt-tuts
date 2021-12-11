from tkinter import *
from calendar import calendar


# lets create function to display calendar
def showCalendar():
    cal_gui = Tk()
    year = int(input.get())
    cal_gui.title(f"{year} Calendar")
    cal_gui.geometry("900x900")

    heading2 = Label(cal_gui, text=f"{year} Calendar", font=("Times", 30, "bold"))
    heading2.grid(row=0, column=0)

    show_calendar = Label(cal_gui, text= calendar(year), font=("Times", 13, "bold"))
    show_calendar.grid(row=1, column=0, padx=30, pady=30)

    cal_gui.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.title("Gui Calendar Using Python (Tkinter)")
    root.geometry("300x300")

    heading = Label(root, text="Python Calendar", font=("Times", 20, "bold"))
    heading.grid(row=0, column= 0)

    title = Label(root, text="Enter Year : ", font=("Times", 10))
    title.grid(row=1, column=0)

    input = Entry(root, width=30)
    input.grid(row=2, column=0)

    show_btn = Button(root, text="Show Calender", command=showCalendar)
    show_btn.grid(row=3, column=0)


    root.mainloop()