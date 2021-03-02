# Selection sort algorithm:
# Description: Selection sort sorts an array by repeatedly finding the minimum element.

class SelectionSort:
    def selection_sort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[i]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr