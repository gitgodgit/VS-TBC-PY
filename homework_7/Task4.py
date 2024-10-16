choice = input("Enter action (e/d): ")

first_row = "qwertyuiop"
second_row = "asdfghjkl"
third_row = "zxcvbnm"


if choice == 'e':
    word = input("Enter text: ")
    for i in range(len(word)):
        if word[i] == 'p':
            print("q", end="")
        elif word[i] == 'l':
            print("a", end="")
        elif word[i] == 'm':
            print("z", end="")
        elif first_row.find(word[i]) != -1:
            print(first_row[first_row.index(word[i]) + 1], end="")
        elif second_row.find(word[i]) != -1:
            print(second_row[second_row.index(word[i]) + 1], end="")
        elif third_row.find(word[i]) != -1:
            print(third_row[third_row.index(word[i]) + 1], end="")
        
        else:
            print(word[i])
        
elif choice == 'd':
    word = input("Enter text: ")
    for i in range(len(word)):
        if word[i] == 'q':
            print("p", end="")
        elif word[i] == 'a':
            print("l", end="")
        elif word[i] == 'z':
            print("m", end="")
        elif first_row.find(word[i]) != -1:
            print(first_row[first_row.index(word[i]) - 1], end="")
        elif second_row.find(word[i]) != -1:
            print(second_row[second_row.index(word[i]) - 1], end="")
        elif third_row.find(word[i]) != -1:
            print(third_row[third_row.index(word[i]) - 1], end="")
        
        else:
            print(word[i])
    
else:
    print("you didnt choose e or d...")