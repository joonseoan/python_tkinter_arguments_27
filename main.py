# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
import tkinter as tk  # built-in lib in python

# Tk for window (canvas)
window = tk.Tk()
window.title("My First GUI Program")
# Minimum size
window.minsize(width=500, height=300)

# Label
# 1) define label
label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
# 2) how to lay out label (It is required to display the label)
# the easiest way of laying out any component is to use `.pack`
# `pack` makes the component automatically placed at the top in the window.
# the default is "top"
# Reference: https://realpython.com/python-gui-tkinter/#the-pack-geometry-manager
label.pack()

"""
.pack() api method does not show us any arguments when we hover the mouth
in the parenthesis. (Also, we can not use the automatic argument name complete when typing the value) why?

It is because `pack()` method uses the `**kw" as argument. (Wider Range of inputs) - Advanced Argument

[Wider Range Argument]

1) default arguments (it is same as Javascript)

In python, when we hove the mouse over the parenthesis, 
we can see required argument and optional argument.
The optional argument has a symbol like "=...". This means that these arguments already have default values. 

2) Unlimited arguments (it is same as Javascript except for "*" mark-based argument name)
Sometimes, we do not know how many arguments are required in a function.
Then, in this case, the number of arguments should be flexible.

# we do not need to use "args" but it is naming convention in python.
def add(*args):
    for n in args:
        print(n)

"""

# left side
label.pack(side=tk.LEFT)  # right
label.pack(side=tk.BOTTOM)  # top
# Takes the entire space of width and height and
# label is centered.
# [IMPORTANT] in this case, "side" does not impact on the label location.
label.pack(expand=True)


# The way of keeping the window open
# It is the same way of turtle.
window.mainloop()

print("")
print("////////////////// UNLIMITED ARGUMENT /////////////////////")


def add(*args):
    print(args)  # It is tuple (In javascript, it is an array)
    num = 0
    for _num in args:
        num += _num

    print(num)


add(1, 2, 3, 5, 7, 5, 45, 45)
