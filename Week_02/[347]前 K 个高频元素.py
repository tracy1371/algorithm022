# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表 
#  👍 596 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
#from heapq import *
from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        res = []
        for n in nums:
            if not n in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        maxpq = PriorityQueue()
        for key, val in dict.items():
            maxpq.put((val,key))
            if maxpq.qsize() > k:
                maxpq.get()
        while not maxpq.empty():
            res.append(maxpq.get()[-1])
        return res
        # 助教，我下面方法用的也是heap，为啥那么慢呢
        # dict = {}
        # res= []
        # for n in nums:
        #     if not n in dict:
        #         dict[n] = 1
        #     else:
        #         dict[n] += 1
        # vallist = list(dict.values())
        # heapify(vallist)
        # for key, val in dict.items():
        #     if val in nlargest(k, vallist):
        #         res.append(key)
        # return res



# leetcode submit region end(Prohibit modification and deletion)
