# Valid Anagram
https://neetcode.io/problems/is-anagram/question

![Easy](https://img.shields.io/badge/easy-4ec9bo?style=for-the-badge&logo=leetcode&logoColor=white)

*Given two strings s and t, return `true` if the two strings are anagrams of each other, otherwise return `false`.*

*An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.*

Example 1:
```python
Input: s = "racecar", t = "carrace"

Output: True
```

Example 2:
```python
Input: s = "jar", t = "jam"

Output: False
```

Constraints:
- `s` and `t` consist of lowercase English letters.

Recommended Time & Space Complexity: O(n + m) & O(1) since we have at most 26 different characters.

Approach: Hashing (Hash Table)
___
