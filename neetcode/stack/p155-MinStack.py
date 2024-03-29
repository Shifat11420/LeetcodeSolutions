# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Complexity: O(1) each operation
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []   # adds minimum value at every level

    def push(self, val:int) -> None:
        self.stack.append(val)
        minvalue = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(minvalue)

    def pop(self)-> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self)-> int: 
        return self.stack[-1]

    def getMin(self)-> int:
        return self.minstack[-1]           

input = ["MinStack","push","push","push","getMin","pop","top","getMin"]
new = MinStack


print(new().push(2))

print(new().push(-2))

print(new().push(3))
# print(new().top())

res = new().getMin()
print(res)