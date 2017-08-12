class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
          #http://www.cnblogs.com/zuoyuan/p/3773134.html
          m=len(word1)+1; n=len(word2)+1
          dp = [[0 for i in range(n)] for j in range(m)]
          delCost = insCost = subCost = 1        # The cost for each operation
          
          for i in range(m):
             dp[i][0]=i
         for j in range(n):
             dp[0][j]=j
         
         for i in range(1,m):
             for j in range(1,n):
                 # del                      insert                      same                             sub
                 #dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
                 dp[i][j]=min(dp[i-1][j] + insCost, dp[i][j-1] + delCost, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else subCost))
         return dp[m-1][n-1]
