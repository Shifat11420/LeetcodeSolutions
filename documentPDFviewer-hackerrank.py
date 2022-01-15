#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
# problem description https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


def designerPdfViewer(h, word):
    # Write your code here
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    wordlist = list(word)
    heights = []
    for i in range(len(wordlist)):
        for j in range(len(letters)):
            if wordlist[i]== letters[j]:
                heights.append(h[j])
            else:
                pass
 
    
    maxheight = max(heights)
    lengthofword = len(wordlist)
    result = maxheight * lengthofword
    return result            

'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
'''

h =[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = 'abc'
result = designerPdfViewer(h, word)

print("Result is : ", result)