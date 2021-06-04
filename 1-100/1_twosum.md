# 1. Two sum #
https://leetcode-cn.com/problems/two-sum/
## Example:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element **twice**.You can return the answer in any order.

**示例:**

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Output: Because nums[0] + nums[1] == 9, we return [0, 1].


```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i,x in enumerate(nums):
            if target-x in hm:
                return [hm[target-x],i]
            hm[x]=i
```