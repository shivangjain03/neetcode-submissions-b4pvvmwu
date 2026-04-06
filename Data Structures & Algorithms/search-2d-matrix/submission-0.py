class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute force:
        #i) Flatten the 2D matrix to 1D list
        #ii) Apply binary search and then search

        flat_list = [item for row in matrix for item in row]
        print(flat_list)
        low = 0
        high = len(flat_list)-1
        while low<=high:
            mid = (high+low)//2
            if flat_list[mid] == target:
                return True
            elif flat_list[mid] < target:
                low = mid+1
            else:
                high = high-1
        return False

