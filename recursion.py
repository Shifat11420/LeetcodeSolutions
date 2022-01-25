#  Write a Python program to calculate the harmonic sum of n-1. Go to the editor
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# harmonic series

# problem 8 : https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php


def harmonic_sum(n):

    if n < 2:
        return 1
    else:
        return (1/n)+ harmonic_sum(n-1)        




if __name__ == '__main__':
    print(harmonic_sum(10))