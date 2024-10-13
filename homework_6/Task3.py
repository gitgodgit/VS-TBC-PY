n = int(input("number 1 - 9999: "))
 
if n > 9 and n < 100:
    reverse = (n % 10) * 10 + int(n / 10)
elif n > 99 and n < 1000:
    reverse = (n % 10) * 100 + (int(n / 10) % 10) * 10 + int(n / 100)
elif n > 999 and n < 10000:
    reverse = (n % 10) * 1000 + (int(n / 10) % 10) * 100 + (int(n / 100) % 10) * 10 + int(n / 1000)
elif n < 10:
    reverse = n




sum = n % 10 + int(n / 10) % 10 + int(n / 100) % 10 + int(n / 1000) % 10 

print("reversed number is: ", reverse)
print("sum of digits: ", sum )