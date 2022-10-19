// Given two integers a and b, return the sum of the two integers without using the operators + and -.

// Example 1:
// Input: a = 1, b = 2
// Output: 3

// Example 2:
// Input: a = 2, b = 3
// Output: 5
 
// # python integers are arbitrarily larger, not 32 bits, so this algorithm runs into problems, hence using JAVA 

// # XOR and bit manipulation
// # & for the carry from (1 XOR 1), shift it to the right
// # loop the process until & returns all zeroes
// # Complexity: time O(1), worst for big numbers O(n)

class Solution {
    public int getSum(int a, int b) {
        while (b!=0){
            int tmp = (a&b)<<1;
            a = a ^ b;
            b = tmp;
        }
        return a;        
    }
} 