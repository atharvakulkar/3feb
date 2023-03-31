#!/usr/bin/env python
# coding: utf-8

# 1) Which keyword is used to create a function? Create a function to return a list of odd numbers in the 
# range of 1 to 25. Ans> The keyword used to create a function in Python is "def". Here's the code to create a functio
# n that returns a list of odd numbers in the range of 1 to 25

# In[1]:


def odd_numbers():
    odd_list = []
    for i in range(1, 26):
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list
odd_numbers()


# 2)Why args and kwargs is used in some functions? Create a function each for args and **kwargs to demonstrate their use.

# In[2]:


args and kwargs ar used in  functions to allow them to accept the varying number of arguements.*args is used to send
the nonkeyworderd variable length arguement list to the function .It allows you to pass a variable number of agruements to a function
whic will be  received as a tuple. kwargs is used to pass keyworded variable length of arguments to a function, which will be received as a dictionary.
Here's an example of how you can use args and *kwargs in a function:


# In[3]:


def print_args(*args):
    print("Arguments passed as *args:", args)
    
def print_kwargs(**kwargs):
    print("Arguments passed as **kwargs:", kwargs)


# 3)What is an iterator in python? Name the method used to initialise the iterator object and the method 
# used for iteration. Use these methods to print the
# first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

# In[4]:



An iterator in Python is an object that implements the iterator protocol,
which consists of two methods: iter() and next(). The iter() method is used to 
    initialize the iterator object, and the next() method is used for iteration.


# In[5]:


#example
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

class TopNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            number = numbers[self.counter]
            self.counter += 1
            return number
        else:
            raise StopIteration

print("The first 5 numbers:")
for number in TopNumbers(5):
    print(number)


# 4)What is a generator function in python? Why yield keyword is used? Give an example of a generator function. Ans> A 
# generator function in Python is a function that returns a generator iterator. The yield keyword is used to return a
# value from a generator function and pause the function's execution. When the generator function is called again, it
# resumes execution from where it left off, using the saved state from the last
# call to yield.

# In[6]:


def fibonacci_sequence(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci_sequence(20)

print("Fibonacci sequence:")
for number in fib:
    print(number)       


# Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers

# In[7]:


def prime_numbers():
    yield 2
    primes = [2]
    candidate = 3
    while candidate < 1000:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 2

primes = prime_numbers()

print("The first 20 prime numbers:")
for i in range(20):
    print(next(primes))


# 6.Write a python program to print the first 10 Fibonacci numbers using a while looP

# In[11]:


a,b =0,1
count =0
    
while count<10:
        print(a)
        a,b= b,a+b
        count += 1


# In[ ]:




