"""Question 1. Write a for loop to iterate through the list A = [1, 2, 3, 4, 5, 6]. Square each element of the list in one by one fashion and print them. After the end of the iteration, print - "The sequence has ended"."""


A = [x for x in range(1,7)]

A_result = list(map(lambda x ,:x**2,A))

for i in range(len(A_result)):print(A_result[i])
print("The sequence has ended")