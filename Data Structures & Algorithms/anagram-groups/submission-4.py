class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute force
        dict1 = {}
        for i in strs:
            temp_dict = {}
            for j in i:
                if j in temp_dict:
                    temp_dict[j]+=1
                else:
                    temp_dict[j] = 1
            tuple_key = tuple(sorted(temp_dict.items()))
            # print(tuple_key)

            if tuple_key in dict1:
                dict1[tuple_key].append(i)
            else:
                dict1[tuple_key] = [i]
        # print(dict1)
        
        return list(dict1.values())
        