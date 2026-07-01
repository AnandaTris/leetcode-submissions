class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        desc = sorted(score, reverse=True)
        res=[]
        for i in range(len(score)):
            if score[i] ==desc [0]:
                res.append('Gold Medal')
            elif score[i]== desc[1]:
                res.append('Silver Medal')
            elif score[i]== desc[2]:
                res.append('Bronze Medal')
                
            else:res.append(str(desc.index(score[i])+1))
        return res
        
