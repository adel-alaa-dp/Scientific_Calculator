import tkinter as tk
import math

# Create the main window
window = tk.Tk()
# window.geometry("300x500")
window.title("Scientific Calculator")

# Set the font
button_font = ("Arial", 14, "bold")
entry_font = ("Arial", 20)

# Create the entry field for the calculator
entry = tk.Entry(window, width=25, font=entry_font, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")


# Define the button click functions
def button_click(number):
    current = entry.get()
    if current == "Error":
        entry.delete(0, tk.END)
        current = ""
    if str(number).isdigit():
        entry.delete(0, tk.END)
        entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry.delete(0, tk.END)


def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry.delete(0, tk.END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, tk.END)


def button_divide():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry.delete(0, tk.END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math_operation == "addition":
        entry.insert(0, f_num + float(second_number))

    if math_operation == "subtraction":
        entry.insert(0, f_num - float(second_number))

    if math_operation == "multiplication":
        entry.insert(0, f_num * float(second_number))

    if math_operation == "division":
        try:
            entry.insert(0, f_num / float(second_number))
        except ZeroDivisionError:
            entry.insert(0, "Error")


def button_sqrt():
    number = entry.get()
    try:
        entry.delete(0, tk.END)
        entry.insert(0, math.sqrt(float(number)))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_sin():
    number = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, math.sin(float(number)))


def button_cos():
    number = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, math.cos(float(number)))


def button_tan():
    number = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, math.tan(float(number)))


# Define the buttons
button_sqrt = tk.Button(
    window, text="SQRT", padx=10, pady=5, font=button_font, command=button_sqrt
)
button_sin = tk.Button(
    window, text="SIN", padx=10, pady=5, font=button_font, command=button_sin
)
button_cos = tk.Button(
    window, text="COS", padx=10, pady=5, font=button_font, command=button_cos
)
button_tan = tk.Button(
    window, text="TAN", padx=10, pady=5, font=button_font, command=button_tan
)
button_clear = tk.Button(
    window, text="Clear", padx=10, pady=5, font=button_font, command=button_clear
)
button_divide = tk.Button(
    window, text="/", padx=10, pady=5, font=button_font, command=button_divide
)
button_multiply = tk.Button(
    window, text="*", padx=10, pady=5, font=button_font, command=button_multiply
)
button_subtract = tk.Button(
    window, text="-", padx=10, pady=5, font=button_font, command=button_subtract
)
button_add = tk.Button(
    window, text="+", padx=10, pady=5, font=button_font, command=button_add
)
button_equal = tk.Button(
    window,
    text="Show Results",
    padx=47,
    pady=5,
    font=button_font,
    command=button_equal,
)
button_7 = tk.Button(
    window,
    text="7",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(7),
)
button_8 = tk.Button(
    window,
    text="8",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(8),
)
button_9 = tk.Button(
    window,
    text="9",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(9),
)
button_4 = tk.Button(
    window,
    text="4",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(4),
)
button_5 = tk.Button(
    window,
    text="5",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(5),
)
button_6 = tk.Button(
    window,
    text="6",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(6),
)
button_1 = tk.Button(
    window,
    text="1",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(1),
)
button_2 = tk.Button(
    window,
    text="2",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(2),
)
button_3 = tk.Button(
    window,
    text="3",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(3),
)
button_0 = tk.Button(
    window,
    text="0",
    padx=10,
    pady=5,
    font=button_font,
    command=lambda: button_click(0),
)
button_decimal = tk.Button(
    window,
    text=".",
    padx=22,
    pady=5,
    font=button_font,
    command=lambda: button_click("."),
)

# Place the buttons on the screen
button_sqrt.grid(row=1, column=0)
button_sin.grid(row=1, column=1)
button_cos.grid(row=1, column=2)
button_tan.grid(row=1, column=3)

button_add.grid(row=2, column=0)
button_subtract.grid(row=2, column=1)
button_multiply.grid(row=2, column=2)
button_divide.grid(row=2, column=3)


button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_decimal.grid(row=6, column=0)
button_clear.grid(row=6, column=1)
button_0.grid(row=6, column=2)

button_equal.grid(row=7, column=0)

# Run the main loop
window.mainloop()
