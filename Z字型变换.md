@author: Jiang Rivers
# 题目
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

示例1：
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
> L　　　C　　　I　　　　R
>
> E　T　O　E　　S　I　　I　　G
>
> E　　　D　　　H　　　　N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

示例2:
> 输入: s = "LEETCODEISHIRING", numRows = 4
>
> 输出: "LDREOEIIECIHNTSG"
>
> 解释:
>
> L　　　　　D　　　　　R
>
> E　　　O　E　　　I　　I
>
> E　C　　　I　H　　　　N
>
> T　　　　　S　　　　　G

## 解法：
找规律就可以了

代码：

    class Solution:
        def convert(self, s: str, numRows: int) -> str:
            if numRows<2:return s
            r=['' for i in range(numRows)]
            for idx,item in enumerate(s):
                ridx=idx%(2*numRows-2)
                if ridx>(numRows-1):
                    ridx=(2*numRows-2-ridx)
                r[ridx]+=item
            return ''.join(r)
            
执行用时 :
52 ms
, 在所有 python3 提交中击败了
98.18%
的用户
内存消耗 :
12.7 MB
, 在所有 python3 提交中击败了
99.83%
的用户

注意r=['' for i in range(numRows)]这段代码的使用，
达到了产生多个字符串的列表效果。

