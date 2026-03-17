class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # res = []
        # for i in range(len(nums)):
        #     p = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         p *= nums[j]
        #     res.append(p)
        # return res

        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n - 1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 4, 6]))  # Output: [48, 24, 12, 8]
    print(solution.productExceptSelf([-1, 0, 1, 2, 3]))  # Output: [0, -6, 0, 0, 0]

## -- Time & Space Complexity -- ##
## Time Complexity: O(n)
## Space Complexity: O(n)
## ---------------------------- ##
