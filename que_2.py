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