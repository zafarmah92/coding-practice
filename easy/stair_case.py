class Solution:
    
    def __init__(self):
        self.mem = [-1]*46 
    def climbStairs(self, n: int) -> int:
        if self.mem[n] != -1 :
            return self.mem[n]
        if n == 1 :
            return 1 
        if n == 2 :
            return 2 
        else :
            self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.mem[n] 
            
