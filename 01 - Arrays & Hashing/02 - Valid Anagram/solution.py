class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_of_s, count_of_t = {}, {}

        for i in range(len(s)):
            count_of_s[s[i]] = 1 + count_of_s.get(s[i], 0)
            count_of_t[t[i]] = 1 + count_of_t.get(t[i], 0)

        return count_of_s == count_of_t


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("racecar", "carrace"))  # Output: True
    print(solution.isAnagram("jar", "jam"))  # Output: False


## -- Time & Space Complexity -- ##
## Time Complexity: O(n + m)
## Space Complexity: O(1)
## ---------------------------- ##
