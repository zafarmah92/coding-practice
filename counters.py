def solution(A):
    # write your code in Python 3.6
    print(sum(range(len(A))) )
    return sum(range(len(A)+1)) - sum(A)
    

A = [1, 2, 3]

print(solution(A))