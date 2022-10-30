
class Solution:
    def __init__(self) :
        pass 

    def isPalindrome(self,x:int) -> bool:
        """
        Palindrome based on the number either its or not 
        """
        temp=x
        rev=0
        while(x>0):
            dig=x%10
            print(dig)
            rev=rev*10+dig
            print(rev)
            x=x//10
            print(x)
        if(temp==rev):
            print("The number is a palindrome!")
        else:
            print("The number isn't a palindrome!")
        return False

if __name__ == '__main__':
    s= Solution()
    s.isPalindrome(121)

        
