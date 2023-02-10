

numbers = [1,2,2,4,3,3,2,4,5,6,5,4]
count = {}
max_rep = 2
new_numbers = []
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

    if count[num] <= max_rep:
        new_numbers.append(num)

print(new_numbers)

#Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
#For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
#With list [20,37,20,21] and number 1, the result would be [20,37,21].


