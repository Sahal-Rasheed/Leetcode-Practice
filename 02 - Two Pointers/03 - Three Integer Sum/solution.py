class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # sort the array to use two pointers 2 sum approach
        nums.sort()

        for i, a in enumerate(nums):
            # skip same element to avoid duplicates in the result
            if i > 0 and a == nums[i - 1]:
                continue

            # two sum approach with two pointers
            l, r = i + 1, len(nums) - 1  # noqa
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1  # noqa
                else:
                    res.append([a, nums[l], nums[r]])
                    # if we found a triplet, we need to move the left pointer to the right and skip same elements to avoid duplicates in the result, because the array is sorted, we can skip all the same elements by moving the left pointer to the right until we find a different element
                    # if only one triplet combination of a element was needed we could have break the loop here
                    l += 1  # noqa
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1  # noqa

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
    print(solution.threeSum([0, 1, 1]))  # Output: []
    print(solution.threeSum([0, 0, 0]))  # Output: [[0, 0, 0]]

## -- Time & Space Complexity -- ##
## Time Complexity: O(n^2)
## Space Complexity: O(1) or O(n)
## ---------------------------- ##
