# Zero Division Error handling with any integer input

n = int(input())
new = []
for i in range(n):
    list_input = input().split()
    new.append(''.join(list_input))
    
for i in range(len(new)):
    try:
        print(int(new[i][0]) // int(new[i][1]))
    except ZeroDivisionError as s:
        print("Error Code:", s)
    except ValueError as s:
        print("Error Code:", s)
