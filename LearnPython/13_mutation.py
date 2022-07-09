def mutate_string(string, position, character):
    list_1 = list(string)
    list_1[position]= character
    return "".join(list_1)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)