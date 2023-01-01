class Solution:
    def longestPalindrome(self, s: str) -> str:
        reverse = s [:: -1]
        if len(s) <= 1 or reverse == s :
            return s 
        else :
            
            listOfPalindromes=[]
            p_string = ""
            for i in range(0,len(s)):
                if s[i] == reverse[i]:
                    p_string += s[i]
                else :
                    listOfPalindromes.append(p_string)
                    p_string=""
            if p_string != "":
                listOfPalindromes.append(p_string)
            if len(set(listOfPalindromes)) <= 1 :
                return s[0]
            else :
                return max(listOfPalindromes)


