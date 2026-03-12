# Group Anagrams

https://neetcode.io/problems/anagram-groups/question

![Medium](https://img.shields.io/badge/medium-f5a623?style=for-the-badge&logo=leetcode&logoColor=white)

*Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.*

*An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.*

Example 1:
```python
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

Example 2:
```python
Input: strs = [""]

Output: [[""]]
```

Example 3:
```python
Input: strs = ["x"]

Output: [["x"]]
```

Constraints:
- `strs[i]` consists of lowercase English letters.

Recommended Time & Space Complexity: O(m * n) & O(m)

Approach: Hashing (Hash Table)
___

