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
# `pack` makes the component automatically placed at the top in the window.
# the default is "top"
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
# 1) when the button is required to be placed after text input
# button = tk.Button(text="Click Me", command=click_me)
# button.pack()

print("")
# ################# Text
text = tk.Text(height=5, width=30)

# Puts cursor in textbox.
text.focus()

# Adds some text to begin with.
# "2.0": just identifier
text.insert("2.0", "Example of multiline text entry")

# "1.0": starting from the first line at the character zero.
# "2.0": just identifier
#  Get's current value in textbox at line 1, character 0
print(text.get("1.0", "2.0"))
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

"""
label.pack() api method (above) does not show us any arguments when we hover the mouth
in the parenthesis. (Also, we can not use the automatic argument name complete when typing the value) why?

It is because `pack()` method uses the `**kw" as argument. (Wider Range of inputs) - Advanced Argument

[Wider Range Argument]

1) default arguments (it is same as Javascript)

In python, when we hove the mouse over the parenthesis, 
we can see required argument and optional argument.
The optional argument has a symbol like "=...". This means that these arguments already have default values. 

2) Unlimited arguments (it is same as Javascript except for "*" mark-based argument name)
Sometimes, we do not know how many arguments are required in a function.
Then, in this case, the number of arguments (which is [IMPORTANT] tuple type) should be flexible.


# we do not need to use "args" but it is naming convention in python.
def add(*args):
    for n in args:
        print(n)
        
3) Many keyworded arguments (**kwargs)
It is going to allow us to work with an arbitrary number of keyword arguments.
[IMPORTANT] It is a type dictionary. So `kwargs` has property of the arguments
in the function all.

    # Python cannot destructure in the parameter
    def cal(**kwargs):
        print(kwargs)  # {'add': 1, 'substract': 2, 'multiply': 4}
        print(type(kwargs))  # <class 'dict'>
    
    
    cal(add=1, substract=2, multiply=4)
"""

print("")
print("////////////////// UNLIMITED ARGUMENT /////////////////////")


# [Detail Example for `*args`] // tuple type
def add(*args):
    print(args)  # It is tuple (In javascript, it is an array)
    num = 0
    for _num in args:
        num += _num

    print(num)


add(1, 2, 3, 5, 7, 5, 45, 45)


print("")
print('/////////////////////// MANY KEWWORDED ARGUMENTS ////////////////')


# [Detail Example 1) for `**kwargs`] // dictionary type
def cal(n, **kwargs):
    # 1) properties
    print(kwargs)  # {'add': 1, 'substract': 2, 'multiply': 4}

    # 2) type
    print(type(kwargs))  # <class 'dict'>

    # 3) get the value (kwargs.add ==> xxx, alternatively, we can use .get() method)
    print("add:", kwargs["add"], ", multiply: ", kwargs["multiply"])

    # 4) usage 1
    for (key, value) in kwargs.items():
        print(key, value)

    # 5) usage 2
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


# except for `n`, others are properties in `kwargs`.
cal(n=3, add=1, substract=2, multiply=4)


# [Detail Example 2) for `**kwargs`] // dictionary type

class Car:
    def __init__(self, **kw):
        # [IMPORTANT]
        # 2) Using .get() api
        # if the key "make" does not exist, it won't generate an error. It returns "None"
        # So the instantiator "car = Car(make="Chev", model="GT-R")" does not need to have all arguments
        self.make = kw.get("make")
        self.model = kw.get("model")

        # 1) Using square bracket
        # if the key "make" does not exist, it will generate an error
        # So the instantiator "car = Car(make="Chev", model="GT-R")" needs to have all arguments
        # self.make = kw["make"]
        # self.model = kw["model"]


car = Car(make="Chev", model="GT-R")
print(car.make)
print(car.model)