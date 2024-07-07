'''
String problem
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        for i in range(len(magazine)):#i is index and magazine is string
            if magazine[i] not in dic: #use [] for indexes
                dic[magazine[i]]=1
            else:
                dic[magazine[i]]=1+dic[magazine[i]] #we are done with i
        for i in range(len(ransomNote)): #start new    
            if ransomNote[i] not in dic:
                return False
            else:
                if dic[ransomNote[i]]==0:
                    return False
                else:
                    dic[ransomNote[i]]=dic[ransomNote[i]]-1
        return True