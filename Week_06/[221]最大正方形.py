# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 动态规划 
#  👍 653 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        m = len(matrix)
        n = len(matrix[0])
        side = 0
        dp = [[0] * (n+1) for _ in range(m + 1)]
        #dp方程dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    side = max(dp[i][j],side)
        return side * side
# leetcode submit region end(Prohibit modification and deletion)
