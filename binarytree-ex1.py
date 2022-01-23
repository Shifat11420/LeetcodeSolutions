class binarytree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binarytree(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarytree(data)       

    def in_order_traversal(self):
        elements = []
        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)
        # visit right subtree    
        if self.right:
            elements += self.right.in_order_traversal()

        return elements 

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:                      
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:                      
            if self.right:
                return self.right.search(val)
            else:
                return False 

    
    def find_min(self):
        if self.left == None:
            return self.data
        if self.left:
            return self.left.find_min()         

    def find_max(self):
        if self.right == None:
            return self.data
        if self.right:
            return self.right.find_max()  

    def calculate_sum(self):
        summ = 0
      
        if self.left:
            summ += self.left.calculate_sum()

        summ += self.data 

        if self.right:
            summ += self.right.calculate_sum()    


        return summ   

    def pre_order_traversal(self):

        elements = [self.data]
        #left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        #right tree
        if self.right:
            elements += self.right.pre_order_traversal()    

        return elements

    def post_order_traversal(self):

        elements = []
        #left tree
        if self.left:
            elements += self.left.post_order_traversal()

        #right tree
        if self.right:
            elements += self.right.post_order_traversal()    

        elements.append(self.data)    

        return elements


    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if val > self.data:
                self.right.delete(val)
        else:
            if self.left == None and self.right == None:                
                return None  
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)



        return self    
                     



def build_tree(elements):
    root = binarytree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])  

    return root  








if __name__ == '__main__':
    #elements = [17, 4, 1, 20, 9, 23, 18, 34]
    elements = [15,12,7,14,27,20,23,88 ]
    tree = build_tree(elements)
    travesed_elements = tree.in_order_traversal()
    print(travesed_elements)
    print(tree.search(9))
    print(tree.search(888))

    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    # numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

    print(tree.find_min())
    print(tree.find_max())
    print(tree.calculate_sum())

    #checking
    summ = 0
    for i in elements:
        summ += i
    print(summ)

    pretravesed_elements = tree.pre_order_traversal()
    print(pretravesed_elements)

    posttravesed_elements = tree.post_order_traversal()
    print(posttravesed_elements)

    tree.delete(12)
    print(tree.in_order_traversal())