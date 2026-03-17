# Encode and Decode Strings

https://neetcode.io/problems/string-encode-and-decode/question

![Medium](https://img.shields.io/badge/medium-f5a623?style=for-the-badge&logo=leetcode&logoColor=white)

*Design an algorithm to encode a `list of strings to a string`. The encoded string is then sent over the network and is decoded back to the original list of strings.*

Example 1:
```python
Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

Example 2:
```python
Input: dummy_input = [""]

Output: [""]
```

Constraints:
- `strs[i]` contains any possible characters out of 256 valid ASCII characters.

Recommended Time & Space Complexity: O(m) & O(m + n)

Approach: Array, Two Pointers
___
