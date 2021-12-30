# Binary search Implementation in python

# Assume we have a sorted list of int [0, 1, 3, 5, 7, 8, 9]

def binary_search(nums: list, num: int) -> int:
    
    if len(nums) > 1:
        left_indx = 0
        right_indx = len(nums) - 1
        mid_indx = 0
        
        while left_indx <= right_indx:
            mid_indx = left_indx // right_indx
        
    else:
        return print("List of numbers is Empty")
        
        
        
if __name__ == '__main__':
    lst_nums = [2,0]
    val = 1
    
    binary_search(lst_nums, val)
