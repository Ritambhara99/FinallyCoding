class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1= [p for p in str(x)]
        x2= list(x1)
        x2.reverse()
        if(x1 == x2):
            return True
