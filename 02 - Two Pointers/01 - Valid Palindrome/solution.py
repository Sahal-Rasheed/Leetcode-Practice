class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for l in s:  # noqa
            if l.isalnum():
                string += l.lower()

        if string == string[::-1]:
            return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("Was it a car or a cat I saw?"))  # Output: True
    print(solution.isPalindrome("tab a cat"))  # Output: False

## -- Time & Space Complexity -- ##
## Time Complexity: O(n)
## Space Complexity: O(n)
## ---------------------------- ##
