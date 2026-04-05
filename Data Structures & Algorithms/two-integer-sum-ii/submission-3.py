class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Remember: 1-indexed
        # traverse numbers 
        # rem = target - numbers[i]
        # check what index is rem return i and that index

        # Brute force
        """for i in range(len(numbers)):
            rem = target - numbers[i]
            req = 0
            if rem in numbers and numbers.index(rem) != i:
                req = numbers.index(rem)
                return [i+1, req+1]"""

        # 2 pointers
        l= 0
        r = len(numbers) - 1
        n = len(numbers)
        # for i in range(n):
        while True:
            calc = numbers[l]+numbers[r]
            if calc>target:
                r-=1
            if calc<target:
                l+=1
            if l!=r and calc == target:
                return [l+1, r+1]
            

        