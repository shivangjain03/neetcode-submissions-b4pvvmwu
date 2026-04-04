class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Dict1-> key = string, val = dict of alphabet recurence
    # traverse dict1 and match if diff key have same value then add them in the output list
    # Time complexity = O(n^2)
        dict1 = {}
        output = []
        for i in strs:
            if i in dict1:
                return
            dict2 = {}
            for j in i:
                if j in dict2:
                    dict2[j]+=1
                else:
                    dict2[j]=1
            
            tup2 = tuple(sorted(dict2.items()))
            if tup2 in dict1:
                dict1[tup2].append(i)
            else:
                dict1[tup2] = [i]
        
        for z in dict1:
            output.append(dict1[z])
        
        return output

        