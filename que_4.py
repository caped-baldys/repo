'''Question 4'''

'''touples are immutalble as they do not support item assignment they can only be overridden.'''
tple = (1,2,3,4,5)
try:
    tple[2]  = 5
except:
    print('error')
finally:
    '''over writing'''
    tple = (1,2,5,4,5)
    print(tple)