# [1. Two sum (easy)](https://leetcode-cn.com/problems/two-sum/)
## 题目:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

* You may assume that each input would have `exactly one solution`<br>
* You may not use the same element **twice**.<br>
* You can return the answer in any order.

**示例:**

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Output: Because nums[0] + nums[1] == 9, we return [0, 1].

## 理解：
+ Brute Force: 
    - 枚举法：go through the list to find the target - x
        ```python3
            class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                n = len(nums)
                for i in range(n):
                    for j in range(i + 1, n):
                        if nums[i] + nums[j] == target:
                            return [i, j]
            
                return []
        ```
    - Time Complexity: O(N^2)
    - Space Complexity: O(1)
+ hash table
    - [hash table题目](https://www.geeksforgeeks.org/hashing-data-structure/#basicHashing)
    - [hash table解释](https://python123.io/index/topics/data_structure/hash_table)
    - 使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N) 降低到 O(1)这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。

        ```python3
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                hm={}
                for i,x in enumerate(nums):
                    if target-x in hm:
                        return [hm[target-x],i]
                    hm[x]=i
        ```
    - Time Complexity: **O(N)**
    - Space Complexity: O(N)