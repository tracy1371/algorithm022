学习笔记
1 选择排序
def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_index = i #从最小开始
        for j in range(i + 1, len(nums)): #逐一和最小比较
            if nums[j] < nums[min_index]:
                min_index = j #更新最小元素
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums

2 插入排序
def insert_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i] #当前插入元素
        pre_index = i - 1
        while pre_index >= 0 and nums[pre_index] > current:
            nums[pre_index + 1] = nums[pre_index] #比较的元素大于current元素则后移
            pre_index -= 1 #下一个要比较的元素
        nums[pre_index + 1] = current #比较元素小于current，将current插入在比较元素后面
    return nums

3 冒泡排序
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]: #前面大于后面，交换
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
