'''
    For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
    (i.e., t is concatenated with itself one or more times).
    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

    Q : https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def gcdOfNo(num1, num2):
            rem = 0
            while num2!=0:
                rem = num1%num2
                num1 = num2
                num2 = rem
            return num1
        if str1+str2 == str2+str1:
            a = len(str1)
            b = len(str2)
            gcd = gcdOfNo(a,b)
            return str1[:gcd]
        else:
            return ""