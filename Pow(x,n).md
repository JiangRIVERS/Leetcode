@author: Jiang Rivers

# 题目

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

> 输入: 2.00000, 10
>
> 输出: 1024.00000

示例 2:

> 输入: 2.10000, 3
>
> 输出: 9.26100

示例 3:

> 输入: 2.00000, -2
>
> 输出: 0.25000
>
> 解释: 2-2 = 1/22 = 1/4 = 0.25

说明:

> -100.0 < x < 100.0
>
> n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

# 解法
递归

代码

```
class Solution:
    def myPow(self, x: float, n: int) -> float:      
        def help(r,idx):
            if idx==1:
                return r
            else:
                if idx%2==0:
                    return help(r**2,idx//2) 
                else:
                   return r*help(r**2,idx//2)
 
        if n==0:
            return 1
        if n>0:
            return help(x,n)
        if n<0:
            return help(1/x,-n)
```
执行用时 :
24 ms
, 在所有 Python3 提交中击败了
97.93%
的用户
内存消耗 :
13.1 MB
, 在所有 Python3 提交中击败了
42.89%
的用户

注意：

如果代码最后一行是：
```
return 1/help(x,-n)
```
则会返回超过数组范围的错误。感谢用户：

https://leetcode-cn.com/u/tool080/

的评论：

在计算的过程中，最好转化为乘法计算，而不要用除法。 
否则会出现数组越界或者是除数为0的情况。

将除法改为乘法则运行成功。