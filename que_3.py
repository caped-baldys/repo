'''Question 3. '''

t_1 = (1, 4, 9, 16, 25, 36)
t_modified = tuple((x**2 for x in t_1 ))
print(t_modified[4])
t_sliced = t_modified[1:3]
print(t_sliced)
#or
#t_modified = *(x**2 for x in t_1 ),