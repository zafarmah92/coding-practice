# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid=n//2
        front_problem_type = False 
        last_mid = None
        while (mid >= 0 or mid <= n):
            if not isBadVersion(mid):
                if front_problem_type == False and last_mid != None:
                    return last_mid
                front_problem_type = True
                mid+=1 
                 
            elif isBadVersion(mid):
                if front_problem_type == True:
                    return mid 
                else :
                    last_mid = mid 
                    mid-=1
                
