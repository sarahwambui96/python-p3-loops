#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown > 0 :
        print(countdown)
        countdown-=1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    squared_elements = [integer * integer  for integer in int_list]
    return squared_elements
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else :
            print(i)
    pass
