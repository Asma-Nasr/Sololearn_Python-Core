file = open("/usercode/files/pull_ups.txt")
n = int(input())
list= file.readlines()
#your code goes here
print(list[n])

file.close()
