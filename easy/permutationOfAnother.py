

## check if given two strings are permuation of another 
import numpy as np 
def checkPermutation (s, t):
    if len(s) != len(t):
        return False
    if sorted(s) == sorted(t):
        return True

if __name__ == "__main__":
    print(checkPermutation("abaa","aba"))
    print(checkPermutation('abc','cba'))