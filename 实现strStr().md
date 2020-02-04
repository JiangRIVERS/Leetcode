@author: Jiang Rivers

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
执行用时 :
28 ms
, 在所有 python3 提交中击败了
97.44%
的用户
内存消耗 :
12.9 MB
, 在所有 python3 提交中击败了
99.42%
的用户

    class Solution:
        def strStr(self,haystack, needle):
            haystacksize = len(haystack)
            needlesize = len(needle)
            if needlesize == 0 :
                return 0
            if needlesize > haystacksize:
                return -1

            table = [0 for i in range(needlesize)]

            # PMT
            for i in range(needlesize):
                candicate = needle[:i + 1]
                sizecandicate = len(candicate)
                prefix = [candicate[:j + 1] for j in range(sizecandicate - 1)]
                suffix = [candicate[k + 1:] for k in range(sizecandicate - 1)]
                tableelement = []
                for l in prefix:
                    if l in suffix:
                        tableelement.append(l)
                if len(tableelement) == 0:
                    table[i] = 0
                else:
                    table[i] = len(max(tableelement))
                    
            # KMP
            l=r=0
            while l <= haystacksize - needlesize:
                for i in range(needlesize):
                    if haystack[r] == needle[i]:
                        r+=1
                    else:
                        if l==r:
                            l+=1
                            r=l
                            break
                        else:
                            l += (r - l) - table[r - l-1]
                            r=l
                            break

                    if r - l == needlesize:
                        return l
            return -1
        
超时