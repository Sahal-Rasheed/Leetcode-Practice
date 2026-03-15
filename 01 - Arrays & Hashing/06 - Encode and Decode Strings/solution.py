class Solution:
    def encode(self, strs: list[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encode

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.encode(["Hello", "World"]))  # Output: "5#Hello5#World"
    print(solution.decode("5#Hello5#World"))  # Output: ["Hello", "World"]

## -- Time & Space Complexity -- ##
## Time Complexity: O(m)
## Space Complexity: O(m + n), where m is the sum of lengths of all the strings and n is the number of strings.
## ---------------------------- ##
