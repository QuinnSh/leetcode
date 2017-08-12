class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        aList=[]
        for i in range(len(tokens)):
            if tokens[i]!='+'and tokens[i]!='-'and tokens[i]!='*'and tokens[i]!='/':
                aList.append(int(tokens[i]))
            else:
                a2=aList.pop()
                a1=aList.pop()
                if tokens[i]=='+':
                    a3=a1+a2
                if tokens[i]=='-':
                    a3=a1-a2
                if tokens[i]=='*':
                    a3=a1*a2
                if tokens[i]=='/':
                    a3=a1/a2
                aList.append(a3)
        return aList.pop()
        
