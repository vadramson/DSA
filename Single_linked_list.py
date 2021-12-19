# Single Linkedlist Implementation in Python

class Node(): # Create a data structure call node containing Data and reference to the next   
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList(): # Create a collection of nodes
    def __init__(self):
        self.head = None # head is of type Node, initialized it to None
        
    def insert_at_begining(self, data): 
        node = Node(data, self.head) # Instantiate a new Node object with data reference to the next
        self.head = node
        #print(type(self.head))
        
    def print_lnk_lst(self):
        if self.head is None:
            print("Linkled list is Empty")
            return
        else:
            nodes = self.head
            lnk_lst = ""
            
            while nodes:
                lnk_lst += str(nodes.data)+" --> "
                nodes = nodes.next
            print(lnk_lst)
            return
        
    # Inserting a new Node at the End of the list
    
    def insert_at_end(self, data):
        if self.head is None: # If the linked list collection is Empty
            self.head = Node(data, None) # Add a new Node to it with None as next since it is the last node
            
        else:
            lnk_lst = self.head
            
            while lnk_lst.next: # while the collection still contains elements...
                lnk_lst = lnk_lst.next # Keep iterating over the collection till the end
            lnk_lst.next = Node(data, None) # Add a new node at the end of the collection 
    
    # Creating a Linked list from a list of data adding new data at the end and clearing any existing linked list
    
    def insert_lists_at_end(self, data):
        self.head = None # Clears any existing linlked list
        for i in data:
            self.insert_at_end(i)
    
    # Creating a Linked list from a list of data adding new data at the begining and clearing any existing linked list
    def insert_lists_at_begining(self, data):
        self.head = None
        for i in data:
            self.insert_at_begining(i)
    
    # Counting the number of items in the linked list
    
    def count_num_nodes(self):
        ct = 0
        
        lnk_lst = self.head
        while lnk_lst:
            ct += 1
            lnk_lst = lnk_lst.next
        return ct
     
if __name__ == '__main__':
    lnk = LinkedList()
    lnk.insert_at_begining(5)
    lnk.insert_at_begining(50)
    lnk.insert_at_begining(58)
    lnk.insert_at_end(13) # This should give 58 --> 50 --> 5 --> 13 -->
    lnk.insert_lists_at_end([12, 30, 95, 26, 92])
    lnk.insert_lists_at_begining([12, 30, 95, 26, 92])
    lnk.print_lnk_lst()
    print("The number of Linked lists is ", lnk.count_num_nodes())
