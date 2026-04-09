class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        dict_main = {}
        for i in strs:
            dict1 = {}
            for j in i:
                if j in dict1:
                    dict1[j] += 1
                else:
                    dict1[j] = 1
            
            dict_tuple = tuple(sorted(dict1.items()))
            if dict_tuple in dict_main:
                dict_main[dict_tuple].append(i)
            else:
                dict_main[dict_tuple] = [i]
        

        for val in dict_main.values():
            output.append(val)
        
        return output

        