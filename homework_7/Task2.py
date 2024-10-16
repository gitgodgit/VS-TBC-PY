word = input("please enter the word of your choice: ")

for i in range(len(word)):
    if word[i] == 'A' or word[i] == 'a' or word[i] == 'E' or word[i] == 'e' or word[i] == 'I' or word[i] == 'i' or word[i] == 'O' or word[i] == 'o' or word[i] == 'U' or word[i] == 'u':
        continue
    else:
        print(word[i], end="")