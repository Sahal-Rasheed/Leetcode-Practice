class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1  # noqa
        res = 0

        while l < r:
            # area is calculated by multiplying the minimum height of the two bars with the distance between them, because the water will be limited by the shorter bar and the width is the distance between the two bars
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1  # noqa
            else:
                r -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1, 7, 2, 5, 4, 7, 3, 6]))  # Output: 36
    print(solution.maxArea([2, 2, 2]))  # Output: 4
    print(solution.maxArea([1, 1]))  # Output: 1
## -- Time & Space Complexity -- ##
## Time Complexity: O(n)
## Space Complexity: O(1)
## ---------------------------- ##
