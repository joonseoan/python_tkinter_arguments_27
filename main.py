# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
import tkinter as tk  # built-in lib in python

# ############################ Tk for window (canvas)
window = tk.Tk()
window.title("My First GUI Program")
# Minimum size
window.minsize(width=500, height=300)
# Adding Padding
window.config(padx=20, pady=20)

# ############################ TK Layout
"""
    How can we set layout?
    Actually, we cannot display the widget without a layout manager.
    [IMPORTANT] Without the layout manager, the widget can't be displayed.
    
    There are three layout managers in TKInter.
    # Reference: https://realpython.com/python-gui-tkinter/#the-pack-geometry-manager
    
    1) Pack: it is provided by each tk api class like Label, Button, Entry, and etc.
        In default, it is placed at center of the top.
        We can change the the location with "side" argument in the pack.
        However, other than the given side value (left, right...), it is complicated
        to place the object at the precise place the developer wants. 

    2) Place: it is able the precise positioning.
        For example, `label.place(x=0, y=0)`
        The downside of Place is, it is so much specific. We should know detail
        information about x and y coordinate values
        
    3) Grid: it is like css grid which has row (horizontal) and column (vertical).
        For example, `label.grid(row=0, column=0)`
        
        [IMPORTANT] the row and column values are relative. So we need to define the first widget.
        Then from that standpoint, we can define the next widget's row and column value.
        
        `label.grid(row=0, column=0)`
        `button.grid(row=1, column=1)`
        `entry.grid(row=2, column=2)`
                
    [IMPORTANT] We cannot set the one and another layout managers at the same time.
"""


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
label.config(text="Old Label")
label.grid(column=0, row=0)

# Since we are using `grid`
# label.pack()

# Adding padding
label.config(padx=50, pady=50)

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
# ####################### TK for button


def click_me():
    # We can still implement the globally defined api call outside this function.

    # 2) Change the label from text_input
    # [IMPORTANT] `text_input` can be here inside this function
    label.config(text=text_input.get())

    # 1) Change label with the hard coded word.
    # label.config(text="I got clicked.")


button = tk.Button(text="Click Me", command=click_me)
button.grid(column=1, row=1)

# Sine we are using `grid`
# button.pack()


def action_for_new_button():
    print("The new button")


new_button = tk.Button(text="New Button", command=action_for_new_button)
new_button.grid(column=2, row=0)

print("")
# ######################## TK for single line text input
text_input = tk.Entry(width=10)
print(text_input.get())
text_input.grid(column=3, row=2)

# Since we are using `grid`
# text_input.pack()

# The way of keeping the window open
# It is the same way of turtle.
window.mainloop()
