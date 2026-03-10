class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.hasDuplicate([1, 2, 3, 3]))  # Output: True
    print(solution.hasDuplicate([1, 2, 3, 4]))  # Output: False


## -- Time & Space Complexity -- ##
## Time Complexity: O(n)
## Space Complexity: O(n)
## ---------------------------- ##
