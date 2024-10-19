first = input("please enter first string: ")
second = input("please enter second string: ")
token = True

if len(first) != len(second):
    token = False
else:
    for i in range(len(first)):
        if first.count(first[i]) == second.count(first[i]) and first.count(second[i]) == second.count(second[i]):
            continue
        else:
            token = False


if token:
    print("YES")
else:
    print("NO")