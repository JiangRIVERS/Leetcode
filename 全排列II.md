@author: Jiang Rivers

# 题目

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

> 输入: [1,1,2]
>
> 输出:
>
> [
>
>   [1,1,2],
>
>   [1,2,1],
>
>   [2,1,1]
>
> ]

# 解法
回溯算法+hashmap去重

代码

``` 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=1:
            return [nums]

        r=[]
        def backstrack(element,pick):
            if not pick:
                r.append(element)
            else:
                hashmap=[]
                for idx,i in enumerate(pick):
                    if i in hashmap:  
                        continue
                    else:
                        hashmap+=[i]
                        backstrack(element+[i],pick[:idx]+pick[idx+1:])
        backstrack([],nums)
        return(r)        
```

执行用时 :
48 ms
, 在所有 Python3 提交中击败了
97.00%
的用户
内存消耗 :
13.6 MB
, 在所有 Python3 提交中击败了
49.02%
的用户

