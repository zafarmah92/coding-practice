## write code about unique characater in the string . 


# Complexity O(N)
# Space compelxity O(1) 

def find_Unique_String(st):
    #print(set(_string))
    char_st = [False] * 128
    #print(char_st)
    for i in range(0, len(st)):
        val = ord(st[i])
        if char_st[val]:
            return False
        char_st[val] = True
    
    return True


if __name__ == "__main__":
    print(find_Unique_String("abc"))