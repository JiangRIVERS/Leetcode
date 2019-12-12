"""
Filename:test.py
A Python3 document for testing leetcode

@author: Jiang Rivers
"""

def lengthOfLongestSubstring(s):
    start=1
    end=1
    ans=0
    map={}
    for i in range(len(s)):
        if s[i] not in map:
            map[s[i]]=start
            ans=max(end-start+1,ans)
            end+=1
        else:
            start




