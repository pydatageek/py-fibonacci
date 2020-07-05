# Fibonacci Series

### Fibonacci Series is a list of numbers in which one number on the series is the sum of the previous two numbers.

    def fibonacci(end=None, start=0, inclusive=True, length=None):
        ...

### Installation and usage
pip install py-fibonacci

from fibonacci import fibonacci

e.g. fibonacci(39) -> returns a list, you may assign it to a variable or print it.

### This python package of fibonacci series, provides two use cases:

1. With an 'end' number argument:: so it is possible to list the fibonacci series up to that number and start (*default: 0*) number argument is optional. An optional boolean inclusive (*default: True*) argument makes the end number inclusive or exclusive.
    
examples: 

    fibonacci(39) 
        -> only end number is given. there are several fibonacci numbers upto 39 starting at 0.

    fibonacci(39, 3) 
        -> end and start numbers are given. there are several fibonacci numbers upto 39 starting at 3.

    fibonacci(39, 3, False) 
        -> end, start numbers and inclusive=False are given. there are several fibonacci numbers upto 39 (exclusive) starting at 3.


2. With a 'length' number argument:: so it is possible to set the length of the series and start (*default: 0*) number argument is optional. 

examples: 

    fibonacci(length=20) 
        -> only length of the series is given. there are 20 fibonacci numbers starting at 0.

    fibonacci(start=5, length=20) 
        -> start number and length of the series is given. there are 20 fibonacci numbers starting at 5.