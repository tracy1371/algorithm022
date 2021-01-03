# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 464 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        if n == k:
            return [[i for i in range(1, n + 1)]]
        if n < k or n < 1:
            return []
        res = []
        def dfs(i, temp):
            if len(temp) == k:
                res.append(temp)
            for j in range(i, n + 1):
                dfs(j + 1, temp + [j])
        for i in range(1, n - k + 2):
            dfs(i + 1, [i])
        return res

# leetcode submit region end(Prohibit modification and deletion)
