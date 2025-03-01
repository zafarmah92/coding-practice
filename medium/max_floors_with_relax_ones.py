class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        sequence = []
        big_sequence = []
        for floor in range (bottom , top+1):
            #print(floor)
            if floor not in special :
                sequence.append(floor)
            else:
                big_sequence.append(sequence)
                sequence = []
        if sequence:
            big_sequence.append(sequence)
        #print(big_sequence)
        #print()
        return len(max(big_sequence, key=len))
