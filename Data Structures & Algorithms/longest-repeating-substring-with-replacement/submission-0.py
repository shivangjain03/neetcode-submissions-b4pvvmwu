class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time complexity = O(n)
        #Valid window = window_size-count of most freq char<=k
        count = {}
        l,max_f,result = 0,0,0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
            max_f = max(max_f, count[s[r]])

            if (r-l+1)-max_f>k:
                count[s[l]]-=1
                l+=1
                
            result = max(result,r-l+1)
        return result



        