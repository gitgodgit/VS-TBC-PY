word = input("please enter a word of your choice: ")
i = 0
max = 5
if len(word) % 2 == 0:
    print(word[int(len(word) / 2) - 1])
    print(word[int(len(word) / 2)])
else:
    while i < max:
        print(word[-1])
        print(word[0])
        print(word[int(len(word) / 2)])
        i += 1
