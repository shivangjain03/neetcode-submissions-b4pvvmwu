class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        l1 = []
        dict_main = {}
        for i in strs:
            dict1 = {}
            for j in i:
                if j in dict1:
                    dict1[j]+=1
                else:
                    dict1[j] = 1
            
            tuple_dict = tuple(sorted(dict1.items()))
            if tuple_dict in dict_main:
                dict_main[tuple_dict].append(i)
            else:
                dict_main[tuple_dict] = [i]
        
        for val in dict_main.values():
            l1.append(val)
        
        return l1

            
            

