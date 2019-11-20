# -*- coding=utf-8 -*-
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
'''


def sumtwo(nums, target):
    lens = len(nums)
    j = -1
    for i in range(nums):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i] == 1) & (target - nums[i] == nums[i])):
                continue
            else:
                j = nums.index(target - nums[i], i + 1)
                break
    if j > 0:
        return [i, j]
    else:
        return []


num = [1, 2, 3, 4, 5, 6]
print(sumtwo(num, 5))
