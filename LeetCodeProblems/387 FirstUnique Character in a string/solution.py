#Code performed in Python. 
class Solution(object):
    def firstUniqChar(self, s):
        for letter in s:
            count = s.count(letter)
            if count < 2:
                return(s.index(letter))
                break
        return -1 
        
