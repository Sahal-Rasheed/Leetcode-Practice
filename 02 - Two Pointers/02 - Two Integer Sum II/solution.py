class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1  # noqa

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1  # noqa
            else:
                return [l + 1, r + 1]
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([1, 2, 3, 4], 3))  # Output: [1, 2]
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]

## -- Time & Space Complexity -- ##
## Time Complexity: O(n)
## Space Complexity: O(1)
## ---------------------------- ##
