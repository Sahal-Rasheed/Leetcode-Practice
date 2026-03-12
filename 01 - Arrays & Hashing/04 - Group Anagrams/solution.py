from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                count[index] += 1
            res[tuple(count)].append(s)
        return list(res.values())


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    )  # Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    print(solution.groupAnagrams([""]))  # Output: [[""]]
    print(solution.groupAnagrams(["x"]))  # Output: [["x"]]


## -- Time & Space Complexity -- ##
## Time Complexity: O(m * n)
## Space Complexity: O(m), where m is the number of strings and n is the length of the longest string.
## ---------------------------- ##
