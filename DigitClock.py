# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import  Tk
from tkinter import Label
import  time


root = Tk()
root.title("Clock")
def theTime():
    display_time = time.strftime("%I:%M:%S %p")
    digit_clock.config(text=display_time)
    digit_clock.after(200,theTime)
digit_clock = Label(root, font=("arial", 145), bg='blue',fg='black')
digit_clock.pack()
theTime()
root.mainloop()
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
