class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute force:
        #i) Flatten the 2D matrix to 1D list
        #ii) Apply binary search and then search

        """flat_list = [item for row in matrix for item in row]
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
                high = mid-1
        return False"""


        # Skip falttenign just consider this as a 1D list
        low = 0
        num_row = len(matrix)
        num_col = len(matrix[0])
        print(num_row)
        print(num_col)
        high = (num_col*num_row)-1
        print(high)
        while low<=high:
            mid = (high+low)//2
            if matrix[mid//num_col][mid%num_col] == target:
                return True
            elif matrix[mid//num_col][mid%num_col] < target:
                low = mid+1
            else:
                high = mid-1
        return False


