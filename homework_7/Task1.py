a = input("please enter a word of your choice: ")

for i in range(len(a)):
    if i % 2 == 0 and a[i] != 'e':
        print(a[i])