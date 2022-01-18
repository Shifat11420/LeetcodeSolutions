class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) :
        self.head = None             #create empty linkedlist

    def print(self):
        itr = self.head
        llstr = ''
        
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'        
            llstr += str(itr.data)+suffix
            itr = itr.next
        print(llstr)     

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next     
        return count      

    def insert_at_beginning(self, data):    
        node = Node(data,self.head)
        self.head = node    

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_at(self, index, data):    
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index") 

        if index == 0:
            self.insert_at_beginning(data)
            return


        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node 
                break 
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index <0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next 
            count += 1   

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)      

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                print("data_after found at index ", count)
                break
            itr = itr.next
            count += 1
        # Now insert data_to_insert after data_after node
        self.insert_at(count+1, data_to_insert)

    def remove_by_value(self, data):
        # Remove first node that contains data 
        itr = self.head
        count = 0
        while itr:   
            if itr.data == data:
                print("first node that contains data is at index ", count)
                break
            itr = itr.next
            count +=1     

        if itr:           
            self.remove_at(count)    
        else:
            raise Exception("data not found")


    '''   solution given

        def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
    '''        

if __name__== '__main__':
    #root = LinkedList()
    # root.insert_at_beginning(5)
    # root.insert_at_beginning(10)
    # #root.insert_at_beginning(15)
    # root.insert_at_beginning(20)
    # root.print()
    # print(root.get_length())
    # root.insert_at_end(77)
    # root.insert_at_end(79)
    # root.insert_at_beginning(20)
    # root.print()
    # root.insert_at(2,11)
    # root.print()
    # root.remove_at(3)
    # root.print()
    # root.insert_values(["mango", "banana", "apple", "grapes"])
    # root.insert_at(1,"pineapple")
    # root.print()
    # root.insert_after_value("apple", "lichi")
    # root.print()
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    pass