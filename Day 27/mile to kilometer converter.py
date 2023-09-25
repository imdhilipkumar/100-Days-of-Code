from tkinter import *

# object creation
window = Tk()
window.title("Miles to Kilometer")

window.config(padx=20, pady=20)


# calculate the miles to kilometer
def calculate():
    miles = float(mile_input.get())
    kilometer = round(miles * 1.609)
    result.config(text=f"{kilometer}")


# input
mile_input = Entry()
mile_input.config(width=7)
mile_input.grid(row=1, column=1)
# output
kilometer = Label(text="Miles")
kilometer.grid(row=1, column=2)

is_equal_to = Label(text="is equal to ")
is_equal_to.grid(row=2, column=0)

result = Label(text="0")
result.grid(row=2, column=1)

kilometer = Label(text="Km")
kilometer.grid(row=2, column=2)
# button
button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=1)

window.mainloop()
