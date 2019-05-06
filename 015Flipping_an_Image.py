# encoding:utf-8
#
#  Algorithm function：
#  Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#  Input:
#  [[1,1,0],[1,0,1],[0,0,0]]
#  Output:
#  [[1,0,0],[0,1,0],[1,1,1]]
#
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #reverse each list
        row=len(A)  #获取当前矩阵中列表个数
        col=len(A[0])  #获取第一个列表中的列表元素个数
        B=[]
        c=[]
        for i in range(row):
            B=A[i]
            B.reverse()   #反转列表元素
            c.append(B)
        for i in range(row):
            for j in range(col):
                if(c[i][j]==1):
                    c[i][j]=0
                else:
                    c[i][j]=1
        return c

if __name__ == '__main__':
    a = Solution().flipAndInvertImage([[1,0,1],[0,1,1],[0,1,1]])
    print(a)

    

