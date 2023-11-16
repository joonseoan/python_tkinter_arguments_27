"""
Each widget in TK has a `pack` method, for instance `label.pack()` and
it does not show us any arguments when we hover the mouth
in the parenthesis.
(Also, we can not use the automatic argument name complete when typing the value) why?

It is because the `pack()` method uses the `**kw" as argument. (Wider Range of inputs) - Advanced Argument

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
        print(kwargs)  # {'add': 1, 'subtract': 2, 'multiply': 4}
        print(type(kwargs))  # <class 'dict'>


    cal(add=1, subtract=2, multiply=4)
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
    print(kwargs)  # {'add': 1, 'subtract': 2, 'multiply': 4}

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
cal(n=3, add=1, subtract=2, multiply=4)


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
