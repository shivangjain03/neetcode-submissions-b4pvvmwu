class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(list(zip(position, speed)), reverse=True)
        count = 0
        st = []
        for p,s in combined:
            time = (target-p)/s
            if len(st) == 0:
                st.append(time)
            if time>st[-1]:
                st.append(time)
        
        return len(st)


        