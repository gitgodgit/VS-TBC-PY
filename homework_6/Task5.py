n = int(input("please enter numebr between 1 - 9: "))
i = 0
j = 0
k = 0


while i <= n:
    j = 0
    while j < n - i:
        print(" ", end = "")
        j += 1
    
    k = i
    while k > 0:
        print(k , end = "")
        k -= 1
    print("0", end = "")

    while k < i:
        print(k + 1, end="")
        k += 1
    print("")
    i += 1

