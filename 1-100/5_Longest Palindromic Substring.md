# [5. Longest Palindromic Substring (Medium)](https://leetcode-cn.com/problems/longest-palindromic-substring/)
## 题目：
Given a string s, return the longest palindromic substring in s.
* 示例:
    - Input: s = "babad"
    - Output: "bab"
    - Note: "aba" is also a valid answer.
<br>
<br>
    - Input: s = "cbbd"
    - Output: "bb"
<br>
* Constraints:
  - 1 <= s.length <= 1000
  - s consist of only digits and English letters (lower-case and/or upper-case),


--------------------------------
## 理解：
* brute force: 
  - 先写一个boolean fuction判断是否为回文字，再遍历所有子串，判断是否回文，保存最长子串
- 动态规划：
  - 用P(i:j)表示字符串s i到j的子串，判断这个子串是否为回文子串
  - 那么我们就可以写出动态规划的状态转移方程：
    - P(i,j)=P(i+1,j−1)∧(Si==Sj)
      - 也就是说，只有 s[i+1:j−1] 是回文串，并且 s 的第 i 和 j 个字母相同时，s[i:j]才会是回文串。
    - 动态规划的边界条件：<br>
      1. P(i,i)=true
      2. P(i,i+1)= (Si == Si+1)
    - 最终的答案即为所有 P(i, j) =true 中 j-i+1（即子串长度）的最大值



--------------------------------
## Code
- 暴力法：超时
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(sub:str):
            return (sub == sub[::-1])
                       
        result = ""
        maxS=0
        l=len(s)
        for i in range(l):
            for j in range(i+1,l+1):
                sub=s[i:j]
                if isPali(sub) and len(sub)>maxS:
                    result=sub
                    maxS=max(maxS,len(sub))
        return result
```
- Time Complexity: 两层循环O(n^2), 判断回文O(n),最后是O(n^3)
- Space Complexity: O(1) 常数个变量

<br>
- 动态规划

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        max_len=1
        begin=0

        dp=[[False]* n for _ in range(n)] #创建matix，表示s[i..j]是否回文
        for i in range(n):
            dp[i][i]=True  #长度为1时一定回文
        
        #开始递推
        #列举sub string长度
        for L in range(2, n+1):
            #枚举左边界上限设置可宽松
            for i in range(n):
                j=L + i - 1 #由L和i确定右边界
                if j>= n:
                    break   #右边界越界
                
                if s[i] != s[j]:
                    dp[i][j]=False
                else: 
                    if j-i <3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1] 

                #只要dp[i][j]=True成立，表示s[i][L]是回文，记录回文长度和起始位置
                if dp[i][j] and j-i+1>max_len:
                    max_len=j-i+1
                    begin=i
        return s[begin:begin+max_len]


```
- Time Complexity: O(n^2)，其中 n 是字符串的长度。动态规划的状态总数为 O(n^2)，对于每个状态，我们需要转移的时间为 O(1)
- Space Complexity: O(n^2)，即存储动态规划状态需要的空间
--------------------------------
## 扩展