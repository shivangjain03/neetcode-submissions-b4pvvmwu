class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]: 
        # Backtrackig as using DP will not optimize it as we have to 
        # create the output not count   number of ways
        res = []
        if len(s)>12:
            return []
        
        def backtrack (i, dots, curIP):
            if dots == 3:
                rem = s[i:]
                if 1<=len(rem)<=3 and int(rem)<=255 and not (len(rem) > 1 and rem[0] == '0'):
                    res.append(curIP+rem)
                    return
                else:
                    return
                
            
            for j in range(1,4):
                cur = s[i:j+i]
                if 1<=len(cur)<=3 and int(cur)<=255 and not (len(cur) > 1 and cur[0] == '0'):
                    backtrack(i + j, dots + 1, curIP + cur + ".")
        backtrack(0, 0, "")   
        return res
        

                


            
