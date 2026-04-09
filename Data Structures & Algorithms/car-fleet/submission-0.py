class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(list(zip(position, speed)), reverse=True)
        print(combined)
        time = []
        for p,s in combined:
            finish_time = (target-p)/s
            if len(time) != 0:
                if finish_time>time[-1]:
                    time.append(finish_time)
            else:
                time.append(finish_time)
            
        return len(time)



        
        