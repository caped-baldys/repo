'''Question 7'''

list_a = [1, 2, 3, 4, 5]

try:
    # input non integer value to raise valueerror 
    # input value grater than size of list_a i:e 4
    index = int(input('Index:')) 

    list_a[index]

except IndexError:
    print('error Index')

except ValueError:
    print('error Value')