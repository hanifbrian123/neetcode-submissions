class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        haveDelete = False
        while l < r:
            if s[l] != s[r]:
                if haveDelete:
                    return False
                
                if s[r-1] == s[l]:
                    r-=1
                elif s[l+1] == s[r]:
                    l+=1
                else:
                    return False
                haveDeleted = True
            else:
                l+=1
                r-=1
        return True


"""



"""