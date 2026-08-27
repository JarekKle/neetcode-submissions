class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        no_spaces = ''
        for letter in s:
            if(ord(letter)>=97 and ord(letter)<=122):
                no_spaces += letter
            if(ord(letter)>=48 and ord(letter)<=57):
                no_spaces += letter
        return no_spaces==no_spaces[::-1]