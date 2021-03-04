# Bubble sort algorithm:
# Description: The bubble sort algorithm have two loops. The inner loop compares each item inside the array with the next item. 
# For this reason the loop starts with a -1 to prevent going out of the array bounds. 
# Also after each outer loop iteration the highest/lowest number (depending of the comparing sign) will be pushed to the last position.
# We can decrease the inner loop by (-i) at the end of each outer loop iteration since there is no reason the compare the last numbers of the array that were previously ordered. 

# Bubble sort optimized:
# We can optimize the time complexity O(n^2) of this algorithm by breaking the loop if the order of the array have not changed after completing the inner loop.
# order_changed keeps track if the list has changed or not after completing the inner loop. 
# If there is no change we will brake out of the outher loop and end the algorithm.

class SortingAlgos:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        n = len(arr) 
        for i in range(n):
            order_changed = False
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    order_changed = True
            if order_changed == False: break
        return arr



 