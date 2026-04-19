class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1.have 1st pointer at first letter (index 0)
        #2.have 2nd pointer at last letter (index len-1)
        #3.Compare pointers,and if same move forward and backward, if not return false
        s = ''.join(char.lower() for char in s if char.isalnum())
        pointer1=0
        pointer2=len(s)-1

        while pointer1 < pointer2:
            if s[pointer1].lower()==s[pointer2].lower():
                pointer1 += 1
                pointer2 -= 1
            elif s[pointer1].lower()!=s[pointer2].lower():
                return False
        
        return True