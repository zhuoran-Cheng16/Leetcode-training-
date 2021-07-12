# [9. Palindrome Number(easy)](https://leetcode-cn.com/problems/palindrome-number/)
## 题目：
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


* 示例:
  <br>
  - Input: x = -121
  - Output: false
  - Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

<br>
<br>

* Constraints:
  *  -231 <= x <= 231 - 1

--------------------------------
## 理解：

<br>
too easy. pass
<br>

--------------------------------
## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
                return True
        return False
```
- Time Complexity: 
- Space Complexity: 
  

<br>
<br>

```python
def isPalindrome(self, x: 'int') -> 'bool':
    if x<0 or (x!=0 and x%10==0):
        return False
    right_rev = 0
    while x > right_rev:
        right_rev = right_rev*10 + x%10
        x = x//10
    return x==right_rev or x==right_rev//10
```
- Time Complexity: O(logn)，对于每次迭代，我们会将输入除以 10，因此时间复杂度为 O(logn)。
- Space Complexity: O(1)。我们只需要常数空间存放若干变量。

--------------------------------
## 扩展