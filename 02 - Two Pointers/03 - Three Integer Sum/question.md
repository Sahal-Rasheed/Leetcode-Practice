# Three Integer Sum

https://neetcode.io/problems/three-integer-sum/question

![Medium](https://img.shields.io/badge/medium-f5a623?style=for-the-badge&logo=leetcode&logoColor=white)

*Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i, j and k` are all distinct.*

*The output should not contain any duplicate triplets. You may return the output and the triplets in any order.*

Example 1:
```python
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
```

Example 2:
```python
Input: nums = [0,1,1]

Output: []
```

Example 3:
```python
Input: nums = [0,0,0]

Output: [[0,0,0]]
```

Recommended Time & Space Complexity: O(n^2) & O(1)

Approach: Two Pointers
___
