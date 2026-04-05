class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Remember: 1-indexed
        # traverse numbers 
        # rem = target - numbers[i]
        # check what index is rem return i and that index

        for i in range(len(numbers)):
            rem = target - numbers[i]
            req = 0
            if rem in numbers and numbers.index(rem) != i:
                req = numbers.index(rem)
                return [i+1, req+1]

        