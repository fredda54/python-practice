class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        while L < R:
            while ord(s[L].lower()) not in range(97,122) and ord(s[L].lower()) not in range(48, 57):
                if L==R:
                    break
                L += 1
            while ord(s[R].lower()) not in range(97,122) and ord(s[R].lower()) not in range(48, 57):
                if R==L:
                    break
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True

            
