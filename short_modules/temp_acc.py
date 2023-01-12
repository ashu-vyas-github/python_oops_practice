#!/usr/bin/env python
# -*- coding: utf-8 -*-


def outer():
    global test
    # nonlocal test
    test = 1  # outer scope
    print("Outer test id:", id(test))

    def inner():
        # nonlocal test
        global test
        test = 2  # inner scope
        print("inner:", test)
        print("Inner test id:", id(test))

    inner()
    print("outer:", test)


test = 0  # global scope
outer()
print("global:", test)
print("Global test id:", id(test))


var = [9999, 8888, 7777]


def some_func(var):
    print("In some_func 1", var)
    var = [59, 69, 79, 89]
    print("In some_func 2", var)
    return None


print("Global 1", var)
some_func(var=var)
print("Global 2", var)

print("\n")
print("~#~" * 30)


def counter(start=0):
    n = start
    while True:
        print("print 1", n)
        result = yield n  # A
        print(type(result), result)  # B
        if result == "Q":
            break
        n += 1
        print("print 2", n)


c = counter()
print(next(c))  # C
print()
print(c.send(200))
print()
print(c.send("Wow!"))  # D
print()
print(next(c))  # E
print()
print(c.send("Q"))  # F
print()
print(c.send(200))
print()
print(next(c))
print()
