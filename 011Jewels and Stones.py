#  Algorithm function：
#  Input: J = "aA", S = "aAAbbbb"
#  Output: 3

class Solution(object):
    def numJewelsInStones(self,J,S):
        J = list(J)
        S = list(S)
        List_J = []
        List_S = []
        result = []
        for i in range(len(J)):
            List_J.append(J[i])
        for j in range(len(S)):
            if S[j] not in List_J:
                result.append(S[j])
            else:
                List_S.append(S[j])
        return len(List_S)

a = Solution()
b = a.numJewelsInStones("aA","aAAbbbb")
print(b)



