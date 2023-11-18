my_list = [5, 9, 2, 3, 1]

sum = 0
avg = 0

for num in my_list:
    sum += num

avg = sum / len(my_list)
print(avg)