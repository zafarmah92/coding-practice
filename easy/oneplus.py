class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        return [int(x) for x in str(int("".join(s)) + 1)]
        #res = [int(x) for x in str(num)]
        #print(res)
