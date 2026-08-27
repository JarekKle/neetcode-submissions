class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        no_spaces = ''
        for letter in s:
            if letter.isalnum():
                no_spaces += letter
        return no_spaces==no_spaces[::-1]