class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(char):
            code = ord(char)
            return (
                ord('a') <= code <= ord('z') or
                ord('A') <= code <= ord('Z') or
                ord('0') <= code <= ord('9')
            )
        
        normalised = "".join(
            char.lower() for char in s if is_alphanumeric(char)
        )

        return normalised == normalised[::-1]