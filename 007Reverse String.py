class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

a = Solution().reverseString("A man, a plan, a canal: Panama")
print(a)