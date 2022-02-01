import random
import sys
from datetime import datetime
random.seed(datetime.now())
import re
import ast
from random import randrange
import os


# if str(sys.argv[1]) == "chooseRandom":
# sqdim = randrange(1,100)
# print("sqdim :", sqdim)
# coldim = randrange(1,100)
# print("coldim :", coldim)
# rowdim = sqdim
# print("rowdim :", rowdim)

# print("   ****    ")
# #print("file_path",file_path)
# #ulim = int(sys.argv[1])
# #file_path = "SuperBreakdown.txt"

# matrix1 = [[randrange(1,10) for i in range(sqdim)] for j in range(sqdim)]
# matrix2 = [[randrange(1,10) for i in range(coldim)] for j in range(rowdim)]
# matrix3 = [[ 0 for i in range(coldim)] for j in range(sqdim)]

# for i in range(sqdim):
#     for j in range(coldim):
#         val =[[]]
#         for k in range(rowdim):         
#                 matrix3[i][j] += matrix1[i][k] * matrix2[k][j]        



# print(matrix3)

# print("dimension : ", len(matrix3), len(matrix3[0]))
# print("Finished matmul")


################*******************************************#################

# elif str(sys.argv[1]) == "choose_A_Random_B_Sandbox":
# print("hdgfjhsdg")
mlist = os.listdir("/home/harshini/CloudPlatform/Platformv5/Sandbox/MatrixB")
r = randrange(0,(len(mlist)))
#print(mlist[r])
file1 = open("/home/harshini/CloudPlatform/Platformv5/Sandbox/MatrixB/" + mlist[r], 'r')
Lines = file1.readlines() 
count = 0
# Strips the newline character
for line in Lines:         
        matrix2 = ast.literal_eval(line)
        
            #Converting string to list of strings


i=0
while i<len(matrix2):   #Converting each string element to integer for m1
    j=0
    while j < len(matrix2[0]):
        matrix2[i][j] = int(matrix2[i][j],16)
        j+=1
    i+=1
sqdim = len(matrix2)
#print(sqdim, len(matrix2), len(matrix2[0]))
matrix1 = [[randrange(1,10) for i in range(sqdim)] for j in range(sqdim)]

matrix3 = [[ 0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]



for i in range(len(matrix1)):
    r = []
    for j in range(len(matrix2[0])):
        val =[[]]
        for k in range(len(matrix2)):       
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        r.append(val)
        
#print("matrix3", len(matrix3), len(matrix3[0]))
print(matrix3)
print("Finished matmul")
#   print("Finished matmul")
