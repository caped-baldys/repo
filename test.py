"""Question 1. Write a for loop to iterate through the list A = [1, 2, 3, 4, 5, 6]. Square each element of the list in one by one fashion and print them. After the end of the iteration, print - "The sequence has ended"."""


A = [x for x in range(1,7)]

A_result = list(map(lambda x ,:x**2,A))

for i in range(len(A_result)):print(A_result[i])
print("The sequence has ended")


"""Question 2. If choice of user = 2, print the pattern - > """

a = 5
choice = int(input('Choice->'))
if(choice==1 or choice==2):

    for i in range(a,0,-1):
        print('*'*i)
    if choice == 2:
        for i in range(1,a+1):
            print('_'*i)
else:
    print('Invalid input')



'''Question 3. '''

t_1 = (1, 4, 9, 16, 25, 36)
t_modified = tuple((x**2 for x in t_1 ))
print(t_modified[4])
t_sliced = t_modified[1:3]
print(t_sliced)
#or
#t_modified = *(x**2 for x in t_1 ),




'''touples are immutalble as they cannot be changed at any index they can only be overridden.'''
tple = (1,2,3,4,5)
try:
    tple[2]  = 5
except:
    print('error')
finally:
    '''over writing'''
    tple = (1,2,5,4,5)
    print(tple)
