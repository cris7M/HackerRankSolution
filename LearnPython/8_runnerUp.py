# with using built in methods
# arr=[2, 3, 6, 6, 5]
# print(arr)
# arr.sort()
# test = list(set(arr))
# print(test[-2])

#without using the built in method
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_2 = []
    
    for i in arr:
        if i not in list_2:
            list_2.append(i)
            
    first_runner = list_2[0]
    second_runner = list_2[1]
    
    for i in list_2:
        if i > first_runner:
            second_runner = first_runner
            first_runner = i
        elif i > second_runner and i != first_runner:
            second_runner = i
        
    print(second_runner)
