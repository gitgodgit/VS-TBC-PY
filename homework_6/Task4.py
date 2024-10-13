n = int(input("please enter numebr between 1 - 9: "))
i = 0
j = 0
k = 0


while i < n + 1:
    j = 0
    while j < i:
        print(j + 1, end = "")
        j += 1
    
    print("")
    i += 1

while k < n :
    j = 1
    while j < n - k:
        print( j, end = "")
        j += 1
    
    print("")
    k += 1

