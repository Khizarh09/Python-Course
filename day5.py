numbers = [23,23,12,43,23]
sum = 0
index = 0
for each in numbers:
    sum = each + sum
    index = index + 1
average = sum / index
print(int(average))