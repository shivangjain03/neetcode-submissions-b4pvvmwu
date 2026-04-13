class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dicti = {}
        for i in tasks:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i]=1
        
        max_f = 0
        for i in dicti:
            if dicti[i]>max_f:
                max_f = dicti[i]
        
        max_count = 0
        for i in dicti:
            if dicti[i]==max_f:
                max_count+=1
        
        print(dicti)
        print(max_f)
        print(max_count)

        return max((max_f - 1) * (n + 1) + max_count, len(tasks))

        


        