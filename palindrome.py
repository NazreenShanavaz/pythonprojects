class Solution:
    def palindrome(self,s):
        if s==s[::-1]:
            return True
        else:
            return False

s=input('enter the string:')
sol=Solution()
print(sol.palindrome(s))