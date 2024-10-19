#Input: 2024-03-22T19:17:42.956376+00:00 
#Output: 22-03-2024 7:17:42 +0
time = input("please enter time in given format: ")

print(time[8:10] + "-" + time[5:7] + "-" + time[0:4] + " " + time[11:19] + " " + time[26:27] + time[28:29])
