# Single Linkedlist Implementation in Python  ==>  https://www.youtube.com/watch?v=qp8u-frRAnU

class Node(): # Create a data structure call node containing Data and reference to the next
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
        
class LinkedList(): # Create a collection of nodes
    def __init__(self):
        self.head = None # head is of type Node, initialized it to None
    
    # Inserting a new Node at the Begining of the LLinkedList    
    def insert_at_begining(self, data):
        node = Node(data, self.head) # Instantiate a new Node object with data reference to the next
        self.head = node
        
    
    # Print the linked list to have a visual representation of the collection    
    def print_lnk_lst(self):
        if self.head is None:
            print("The linked List is Empty")
        else:
            lnk_lst = self.head
            lst_data = ""
            
            while lnk_lst:
                lst_data += str(lnk_lst.data) + " --> "
                lnk_lst = lnk_lst.next
                
            print(lst_data)
            
    # get the length of the LinkedList collection
    def get_length(self): # (Helper method)
        ct = 0
        
        lnk_lst = self.head
        
        while lnk_lst:
            ct += 1
            lnk_lst = lnk_lst.next
        return ct
        
    
    # Inserting a new Node at the End of the list    
    def insert_at_end(self, data):
        
        lnk_lst = self.head
        if self.get_length()  == 1: #  If the linked list collection is Empty
            lnk_lst.next = Node(data, None)  # Add a new Node to it with None as next since it is the last node
        
        elif self.get_length() == 0:
            self.head = Node(data, None)
        else:
            cnt = 0
            while lnk_lst: # while the collection still contains elements...
                if cnt == self.get_length() - 1: # Add a new node at the end of the collection 
                    lnk_lst.next = Node(data, None)
                    break
                cnt += 1
                lnk_lst = lnk_lst.next # Keep iterating over the collection till the end
    
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
                
                
    # Delete a node from the Linked list collection at a given index position            
    def delete_at_position(self, pos):
        if (pos < 0) | (pos >= self.get_length()):
            print("Invalid position")
        else:
            lnk_lst = self.head
            
            if pos == 0:
                self.head = lnk_lst.next
            else:
                cnt = 0
                
                while lnk_lst:
                    if cnt == pos-1:
                        lnk_lst.next = lnk_lst.next.next
                        break
                    lnk_lst = lnk_lst.next
                    cnt += 1
    
    
    # Insert a node into the Linked list collection at a given index postion
    def insert_at_pos(self, data, pos): # data -> data to insert | pos -> position to insert the data         
        if pos <= 0:
            self.insert_at_begining(data)
        elif pos >= self.get_length():
            self.insert_at_end(data)
        else:
            cnt = 0
            lnk_lst = self.head
            
            while lnk_lst:
                if cnt == pos-1:
                    lnk_lst.next = Node(data, lnk_lst.next)
                    break
                lnk_lst = lnk_lst.next
                cnt += 1
                
    # insert data into the Linked list collection after a certain value present in the Linked list collection                
    def insert_after_value(self, data, value): # data -> data to insert | value -> value after which to insert the data
        lnk_lst = self.head
        while lnk_lst:
            if lnk_lst.data == value: # do the insert operation
                lnk_lst.next = Node(data, lnk_lst.next) # Loop through the list, when you see the value, assign to it's next a new node containing the new data, with it's next being the next node after the value 
                return
            else:
                lnk_lst = lnk_lst.next
        print("value not found in linked list")
    
    
    # Remove a valuie present in the Linked list collection
    def remove_by_value(self, value): # value to be remove from the linkedlist
        lnk_lst = self.head
        cnt = 0
        while lnk_lst:
            if lnk_lst.data == value: # remove the value from the list
                if cnt == 0:
                    self.head = lnk_lst.next
                    return
                elif cnt != 0:
                    lnk_lst = self.point_to_index_of_collections_before(cnt)
                    lnk_lst.next = lnk_lst.next.next
                    return
            else:
                lnk_lst = lnk_lst.next
                cnt += 1
        print("Value not found in Linkd list")
        
    
    # Return a Linked list collection that points at one index before the given index    
    def point_to_index_of_collections_before(self, indx): # (Helper Method)
        lnk_lst = self.head
        ct = 0
        while lnk_lst:
            if ct == indx-1:
                #print(lnk_lst.next.data)
                return lnk_lst
            else:
                lnk_lst = lnk_lst.next
                ct += 1
        print("No Value at index ", indx)
            
                
    
            
            
            
if __name__ == '__main__':
    lk_lst = LinkedList()
    lk_lst.insert_at_begining(5)
    lk_lst.insert_at_begining(10)
    lk_lst.insert_at_begining(15)
    lk_lst.insert_at_begining(20)
    lk_lst.insert_at_end(90)
    lk_lst.print_lnk_lst() #  This should print 20 --> 15 --> 10 --> 5 --> 90 -->
    lk_lst.point_to_index_of_collections_before(2)
    print('The length of the Linked list is:', lk_lst.get_length())
    #lk_lst.delete_at_position(0)
    lk_lst.insert_at_pos(17,0)
    lk_lst.print_lnk_lst()
    print('The length of the new Linked list is:', lk_lst.get_length())
    lk_lst.insert_after_value(13, 10) # Data | value i.e, Add 13 after 10 
    lk_lst.print_lnk_lst()
    print('The length of the new Linked list is:', lk_lst.get_length())
    print("\n Remove by value \n")
    lk_lst.remove_by_value(13)
    lk_lst.print_lnk_lst()
    print('The length of the new Linked list is:', lk_lst.get_length())
    print("")
    print("\n Creating LinkedList Collection from list of values \n\n")
    lk_lst.insert_lists_at_end([12, 30, 95, 26, 92])
    lk_lst.print_lnk_lst()
    print('The length of the new Linked list is:', lk_lst.get_length())
    lk_lst.insert_lists_at_begining([12, 30, 95, 26, 92])
    lk_lst.print_lnk_lst()
    print('The length of the new Linked list is:', lk_lst.get_length())
                
                
                
