class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        feq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            feq[c].append(n)

        res = []
        for i in range(len(feq) - 1, 0, -1):
            # res.extend(feq[i])
            for num in feq[i]:
                res.append(num)

            if len(res) == k:
                return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))  # Output: [2, 3]
    print(solution.topKFrequent([7, 7], 1))  # Output: [7]

## -- Time & Space Complexity -- ##
## Time Complexity: O(n)
## Space Complexity: O(n)
## ---------------------------- ##
