class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,4,5,6], 7))  # Output: [0,1]
    print(solution.twoSum([4,5,6], 10))  # Output: [0,2]
    print(solution.twoSum([5,5], 10))  # Output: [0,1]


## -- Time & Space Complexity -- ##
## Time Complexity: O(n)
## Space Complexity: O(n)
## ---------------------------- ##
