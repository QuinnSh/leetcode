class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matchDict={'(':')','[':']','{':'}'}
        aList=[]
        strlen=len(s)
        if strlen<=1:
            return False
        else:
            for i in range(strlen):
                if s[i] not in matchDict.keys() and len(aList)==0:
                   return False
                elif s[i] in matchDict.keys():
                   aList.append(s[i])
                elif s[i]==matchDict[aList[-1]]:
                   aList.pop()
                else:return False
            if len(aList)==0:
                return True
            
        
        
        
