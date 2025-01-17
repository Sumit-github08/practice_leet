'''
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
    starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string.

    Q : https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        reverse_string = ""
        i=0
        while i< len(word1) and i<len(word2):
            reverse_string += word1[i] + word2[i]
            i+=1
        if i<len(word1):
            reverse_string += word1[i:]
        if i<len(word2):
            reverse_string +=word2[i:]
        return reverse_string