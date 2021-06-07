# [3. Longest Substring Without Repeating Characters   (Medium)](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

## 题目：
Given a string `s`, find the length of the **longest substring** without repeating characters.

* 示例:<br>
**Input:** s = "abcabcbb"<br>
**Output:** 3<br>
Explanation: The answer is "abc", with the length of 3.

    **Input**: s = "pwwkew"<br>
    **Output**: 3<br>
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


<br>

--------------------------------

## 理解：
1. 首先不能用brute force来做，会超时
2. 滑动窗口解法：
    * 先找出从每一个字符开始的，不包含重复字符的最长substring，其中最长的substring就是答案
    * 使用两个pointer来表示string中某个substring的左右boundary，其中左pointer是起始位置，有pointer为中止位置。
    * 每一步将左pointer向右移动一格，表示开始枚举下一个char作为起始位置，接着不断向右移动右pointer。保证这两个pointer对应的substring没有重复的字符，移动结束后，substring的长度就是对应的答案（以左pointer开始的，不包含重复字符的最长substring）



<br>

--------------------------------
## Code
**暴力法**
* 用两个循环穷举所有s里的substring，再加一个循环判断该子串有没有重复的字符
```java
public int lengthOfLongestSubstring(String s) {
    int n = s.length();
    int ans = 0;//保存当前得到满足条件的子串的最大值
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j <= n; j++) //之所以 j<= n，是因为我们子串是 [i,j),左闭右开
            if (allUnique(s, i, j)) ans = Math.max(ans, j - i); //更新 ans
    return ans;
}

public boolean allUnique(String s, int start, int end) {
    Set<Character> set = new HashSet<>();//初始化 hash set
    for (int i = start; i < end; i++) {//遍历每个字符
        Character ch = s.charAt(i);
        if (set.contains(ch)) return false; //判断字符在不在 set 中
        set.add(ch);//不在的话将该字符添加到 set 里边
    }
    return true;
}
```
- Time Complexity:O(N^3) 
- Space Complexity: O(min(m,n))
     * 使用了一个 set，判断子串中有没有重复的字符。由于 set 中没有重复的字符，所以最长就是整个字符集，假设字符集的大小为 m ，那么 set 最长就是 m 。另一方面，如果字符串的长度小于 m ，是 n 。那么 set 最长也就是 n 了

**滑动窗口**
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         ht={}
         i,res=0,0 
         #判断s[j]相同元素上次出现的位置，和i哪个大，如果i大，说明[i,j-1]中没有与s[j]相同的元素，起始位置仍取i，如果i小，这说明有重复元素，起始位置变为ht[s[j]]
         for j in range(len(s)):
            if s[j] in ht:
                 i=max(ht[s[j]],i)
            res=max(res,j-i+1) #res是前j-1个元素的最长子串，j-i+1是以s[j]结尾的最长子串长度
            ht[s[j]]=j+1
         return res
```
- j表示子串中止位置，i表示起始位置，当未出现重复时，string的长度就是（j-i+1），但发生重复时，从村里用string的结束位置j减去新的起始位置i，与之前为重复的string的长度做比较取最大的
- Time Complexity: O(N),N是字符串长度，左右pointer会遍历整个string一次
- Space Complexity: O(∣Σ∣)，其中 Σ 表示字符集（即字符串中可以出现的字符），∣Σ∣ 表示字符集的大小。
<br>
<br>

--------------------------------
## 扩展
**[滑动窗口算法（sliding window algorithm)](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%8A%80%E5%B7%A7.md)**
+ 滑动窗口算法可以用以解决数组/字符串的子元素问题，它可以将嵌套的循环问题，转换为单循环问题，降低时间复杂度
    - 滑动窗口本质上来源于单调性，一般可以理解为，随着左端点位置的增加，其最优决策的右端点位置单调不减。
    - **滑动**：说明这个窗口是移动的，也就是移动是按照一定方向来的。
    - **窗口**：窗口大小并不是固定的，可以不断扩容直到满足一定的条件；也可以不断缩小，直到找到一个满足条件的最小窗口；当然也可以是固定大小。
+ basic:
    - 设定滑动窗口（window）大小为 3，当滑动窗口每次划过数组时，计算当前滑动窗口中元素的和，得到结果 res
![示例](img/3.png)

    + 可以用来解决一些`查找满足一定条件的连续区间`的性质（长度等）的问题。由于区间连续，因此当区间发生变化时，可以通过旧有的计算结果对搜索空间进行剪枝，这样便`减少了重复计算`，降低了时间复杂度。往往类似于“ 请找到满足 xx 的最 x 的区间（子串、子数组）的 xx ”这类问题都可以使用该方法进行解决。

+ 思路：
1. 我们在字符串 S 中使用双指针中的左右指针技巧，初始化 left = right = 0，把索引闭区间 [left, right] 称为一个「窗口」。

2. 我们先不断地增加 right 指针扩大窗口 [left, right]，直到窗口中的字符串符合要求（包含了 T 中的所有字符）。

3. 此时，我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了）。同时，每次增加 left，我们都要更新一轮结果。

4. 重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头。

    - 第 2 步相当于在寻找一个「**可行解**」，然后第 3 步在优化这个「可行解」，最终找到最优解。左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动。