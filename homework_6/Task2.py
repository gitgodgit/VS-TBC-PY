n = int(input("please enter number 1-100: "))
print(n, end = "")
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    print(" ->",int(n) , end = "")