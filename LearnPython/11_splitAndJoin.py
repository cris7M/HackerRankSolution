def split_and_join(line):
    list_1 = line.split(" ")
    return "-".join(list_1)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)