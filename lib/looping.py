#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count > 0:
        print(count)
        count = count -1
    print("Happy New Year!")   
pass

def square_integers(int_list):
    # code goes here!
    return int_list ** 2
    pass

def fizzbuzz():
    # code goes here!
    
    for num in range(100):
        num = num + 1
        if num % 3 == 0 and num % 5 == 0 :
            print("FizzBuzz")
        elif num % 3 ==0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    pass

