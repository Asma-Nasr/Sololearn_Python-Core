'''
Tom has done pull ups every day and recorded his results.
He recorded each day's results in a new line, so that each line represents each day he has done pull ups.
Create a program that takes n number as input and outputs the n-th days result (starting from 0).

'''file = open("/usercode/files/pull_ups.txt")
n = int(input())
list= file.readlines()
#your code goes here
print(list[n])

file.close()
