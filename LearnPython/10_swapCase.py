def swap_case(s):
    str=""
    for i in range(0, len(s)):
        if s[i].islower():
            str+=s[i].upper()
        else:
            str+=s[i].lower()
    
    return str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)