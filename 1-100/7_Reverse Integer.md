# [7. Reverse Integer(EASY)](https://leetcode-cn.com/problems/reverse-integer/)
## 题目：
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

`Assume the environment does not allow you to store 64-bit integers (signed or unsigned).`

* 示例:
  <br>
  - Input: x = 123
  - Output: 321
<br>
<br>
  - Input: x = -123
  - Output: -321
<br>
* Constraints:-2^31 <= x <= 2^31 - 1
<br>
--------------------------------
## 理解：
1. 暴力反转，利用 [::-1]
2. 数学翻转：记rev 为翻转后的数字，为完成翻转，我们可以重复「弹出」xx 的末尾数字，将其「推入」rev 的末尾，直至 x 为 0。
   - 要在没有辅助栈或数组的帮助下「弹出」和「推入」数字，我们可以使用
   - 弹出 x 的末尾数字 digit
     - digit = x % 10
     - x /= 10

   - 将数字 digit 推入 rev 末尾
     - rev = rev * 10 + digit

<br>

<br>

--------------------------------
## Code
1. 暴力翻转
```python
class Solution:
    def reverse(self, x: int) -> int:
        a=0
        if x>=0:
                a=int(str(x)[::-1])
        if x<0:
                a=-int(str(-x)[::-1])
        return 0 if a<-2**31 or a>2**31-1 else a
```
- Time Complexity: O(1)
- Space Complexity: O(1)

<br>

2. 数学翻转：
```python
class Solution:
    def reverser(self, x: int)-> int:
        MIN,MAX=-2**31, 2**31-1
        res=0
        while x!=0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev<MIN//10+1 or rev>MAX//10:
                return 0
            digit=x%10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x<0 and digit>0:
                digit -=10 
            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x=(x-digit)//10 
            rev=rev*10 +digit 
        return rev 
```
- Time Complexity: O(log|x|)
- Space Complexity: O(1)
--------------------------------
## 扩展