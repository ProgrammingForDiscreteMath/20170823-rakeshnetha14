"""
This is the code file for Assignment from 23rd August 2017.
This is due on 30th August 2017.
"""
##################################################
#Complete the functions as specified by docstrings


# 1
def entries_less_than_ten(L):
    """
    Return those elements of L which are less than ten.

    Args:
        L: a list

    Returns:
        A sublist of L consisting of those entries which are less than 10.
    """
    L1=[x for x in L if x<10]
    return L1 #Add your code here

#Test
#print entries_less_than_ten([2, 13, 4, 66, -5]) == [2, 4, 6, -5]
entries_less_than_ten([2,13,4,66,-5])

# 2

def number_of_negatives(L):
    """
    Return the number of negative numbers in L.

    Args:
        L: list of integers

    Returns:
        number of entries of L which are negative
    """
    l1=len([x for x in L if x<0])
    return l1
    pass ##YOUR CODE REPLACES THIS

# TEST
#print number_of_negatives([2, -1, 3, 0, -1, 0, -45, 21]) == 3
number_of_negatives([2,-1,3,0,-1,0,-45,21])

# 3
import numpy as np
def common_elements(L1, L2):
    """
    Return the common elements of lists ``L1`` and ``L2``.

    Args:
        L1: List
        L2: List

    Returns:
        A list whose elements are the common elements of ``L1`` and
        ``L2`` WITHOUT DUPLICATES.
    """
    L=[x for x in L1 for y in L2 if x==y ]
    return np.unique(L)
    pass # your code goes here

#TEST
#common_elements([1, 2, 1, 4, "bio", 6, 1], [4, 4, 2, 1, 3, 5]) == [1, 2, 4]
common_elements([1,2,1,4,"bio",6,1],[4,4,2,1,3,5])

#4
def fibonacci_generator():
    """                                                                                 
    Generate the Fibonacci sequence.                                                    
                                                                                        
    The Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21,...                                 
    is defined by a1=1, a2=1, and an = a(n-1) + a(n-2).                                 
    """
    a,b=1,1
    for i in range(10):
        yield a
        a,b=b,a+b
    pass # Hint: use the ``yield`` command. 
f=fibonacci_generator()
[f.next() for i in range(10)]

#TEST
#f = fibonacci()
#[f.next() for f in range(10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#5
def largest_fibonacci_before(n):
    """
    Return the largest Fibonacci number less than ``n``.
    """
    pass #Your code goes here.
    a,b=1,1
    while (a<n):
        a,b=b,a+b
    return b-a 

#TEST
#largest-fibonacci_before(55) == 34
largest_fibonacci_before(55)

#6
import math
def catalan_generator():
    """
    Generate the sequence of Catalan numbers.

    For the definition of the Catalan number sequence see `OEIS <https://www.oeis.org/A000108>`.
    """
    pass #Your code goes here.
    for i in range(10):
        yield math.factorial(2*i)/(math.factorial(i)*math.factorial(i+1))
c=catalan_generator()
[c.next() for i in range(10)]
#TEST
#c = catalan_generator()
#[c.next() for i in range(10)] == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    
    
#7
### CREATE YOUR OWN FUNCTION. Make sure it has a nice docstring.
# See https://www.python.org/dev/peps/pep-0257/
# for basic tips on docstrings.

def sum_of_list(L1):
    """
    L1 is an input list

    
    this function adds all the elements of the list
    """
    sum=0
    for i in range(len(L1)):
        sum=sum+L1[i]
    return sum

sum_of_list([10,-3,5,7]
