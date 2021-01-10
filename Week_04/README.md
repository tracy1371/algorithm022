学习笔记
Q:使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
A:1.初始left = 0，right = len（nums）-1。只处理存在反转的部分，因此循环条件nums[left] >= nums[right]
  2.如果nums[mid]大于nums[right]就说明在右半部分不是单调递增的，即在右半部分存在反转，使新left=mid，再次寻找中间值
  3.如果nums[mid]小于nums[right]说明在右半部分单调递增，则反转出现在左半部分，使新right=mid，再次寻找中间值
  4.直到right-left <= 1,此时left=right或left和right相邻。反转的位置为left=right，或nums[left]与nums[right]之间较大的位置。
Python3代码：
class Solution:
	def search(self,nums:List[int]) -> int:
		left , right = 0, len(nums) - 1
       		 while nums[left] >= nums[right]:
            		mid = left + (right - left) // 2
            		if nums[mid] >= nums[right]:
                		left = mid
            		else:right = mid
            		if right - left <= 1:
                		return nums.index(max(nums[right],nums[left]))
最后返回了无序位置的下标
