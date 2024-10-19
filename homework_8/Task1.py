a = input("please enter a string to determine palindrome: ")
a = a.lower()
token = True
letters = "abcdefghijklmnopqrstuvwxyz"
# s da t simboloebis counteria da spacebisac
s = 1
t = 0
length = int(len(a))
half_length = int(length / 2)

for i in range(half_length):
    while a[length - i - s] not in letters:
        s += 1
    while a[i + t] not in letters:
        t += 1
    if a[i + t] == a[length - i - s]:
        continue
    else:
        token = False
if token:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
