class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def generate(para, total1, total2):

            if total1 == total2 and total1 ==n:
                res.append(para)
                return
            
            if total1 < n:
                generate(para+'(', total1 + 1, total2)
            if total2 < total1:
                generate(para + ')', total1, total2 + 1)


        generate('',0,0)
        return res