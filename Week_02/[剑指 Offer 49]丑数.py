# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 
# 
#  
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
# 
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
#  Related Topics 数学 
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        temp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            # n2 = 2, n3 = 3, n5 = 5
            n2, n3, n5 = temp[a] * 2, temp[b] * 3, temp[c] * 5
            # temp[1] = n2
            temp[i] = min(n2, n3, n5)
            # n2已经加入列表，a后移一位
            if temp[i] == n2: a += 1
            if temp[i] == n3: b += 1
            if temp[i] == n5: c += 1
        return temp[-1]





# leetcode submit region end(Prohibit modification and deletion)
