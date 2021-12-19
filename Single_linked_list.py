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
        
if __name__ == '__main__':
    lnk = LinkedList()
    lnk.insert_at_begining(5)
    lnk.insert_at_begining(50)
    lnk.insert_at_begining(58)
    lnk.print_lnk_lst()
        
    
