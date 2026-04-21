class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic = {}
        for i in hand:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        print(dic)
        sorted_dic = dict(sorted(dic.items()))
        print(sorted_dic)

        for i in sorted_dic:
            if sorted_dic[i]!=0:
                count = sorted_dic[i]
                for j in range(i,i + groupSize):
                    if j in sorted_dic and sorted_dic[j]!=0:
                        sorted_dic[j]=sorted_dic[j]-count
                    else:
                        return False  

        return True



        