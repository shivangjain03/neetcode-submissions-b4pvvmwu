class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # Dec Monotonic stack
        st = [] # Storing index
        result = [0]*n # Result list 
        for i in range(n):
            while st and temperatures[i]>temperatures[st[-1]]:
                prev_index = st.pop()
                result[prev_index] = i-prev_index

            st.append(i)
        return result
            



        