# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
import tkinter as tk  # built-in lib in python

# ############################ Tk for window (canvas)
window = tk.Tk()
window.title("My First GUI Program")
# Minimum size
window.minsize(width=500, height=300)

print("")
# ############################# TK for label
# Label
# 1) define label
label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))

# Not working
# label.text = "New Label"

# 1)
label["text"] = "New Label"

# 2)
label.config(text="Label from config")

# 2) how to lay out label (It is required to display the label)
# the easiest way of laying out any component is to use `.pack`
# `pack` makes the component (widget) automatically placed at the top in the window by default.
# Reference: https://realpython.com/python-gui-tkinter/#the-pack-geometry-manager
label.pack()

# Takes the entire space of width and height and
# label is centered.
# [IMPORTANT] in this case, "side" does not impact on the label location.
# label.pack(expand=True, side=tk.LEFT)

# [IMPORTANT] if we set this up in this line, the next line `label.pack(side=tk.BOTTOM)` does not work.
# label.pack(expand=True)

# bottom side
# label.pack(side=tk.BOTTOM)  # top

# left side
# label.pack(side=tk.LEFT)  # right

# Tkinter module is actually imported from another technology called "TK"
# TK actually has a very different syntax from Python. Many of TK api methods / instances
# such as pack and labels, are using "**kwargs"

print("")
# ####################### TK for button to be displayed before text input
button = tk.Button()
button.pack()

print("")
# ######################## TK for single line text input
text_input = tk.Entry(width=10)
# "1": just identifier
# "string" is like a placeholder
text_input.insert(index=1, string="Some text to begin with.")
text_input.pack()

print("")


# ######################## TK for button


def click_me():
    # We can still implement the globally defined api call outside this function.

    # 2) Change the label from text_input
    label.config(text=text_input.get())

    # 1) Change label with the hard coded word.
    # label.config(text="I got clicked.")


button.config(text="Click Me", command=click_me)

# 1) when the button is required to be fully placed after text input
# button = tk.Button(text="Click Me", command=click_me)
# button.pack()

print("")
# ################# Text
text = tk.Text(height=5, width=30)

# Puts cursor in textbox.
text.focus()

# Adds some text to begin with.
# "2.0": just identifier
text.insert("2.0", "Example of multiline text entry\nabc")

# [IMPORTANT]
# "1.0": starting from the first line at the character zero.
# "3.0": ending before line 3 and char position 0
#  Get current value in textbox at line 1, character 0
print(text.get("2.0", "3.0"))
text.pack()

print("")


# ################# Spin box


def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

print("")


# ################# Scale


def scale_used(value):
    print(value)


scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

print("")


# ################# Check button


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tk.IntVar()

checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

print("")


# ######################### Radiobutton


def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()

radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# ####################### Listbox


def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tk.Listbox(height=4)

fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# The way of keeping the window open
# It is the same way of turtle.
window.mainloop()
