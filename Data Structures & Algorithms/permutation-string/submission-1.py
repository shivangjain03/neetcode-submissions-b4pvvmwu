class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def freq_check(s1):
            freq_map = {}
            for i in s1:
                if i not in freq_map:
                    freq_map[i] = 1
                else:
                    freq_map[i]+=1
            return freq_map
        
        freq_s1 = freq_check(s1)
        
        for i in range(len(s2)):
            window = s2[i:(i+len(s1))]
            window_freq = freq_check(window)
            if window_freq == freq_s1:
                return True
            
        
        return False

