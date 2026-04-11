class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Apply binary search on a 2D array
        low = 0
        n = len(matrix[0])
        high = (len(matrix[0])*len(matrix))-1
        while low<=high:
            mid = (low+high)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                low = mid+1
            else:
                high = mid - 1
        return False