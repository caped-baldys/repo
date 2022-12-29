'''question 6'''

list_a = ["car", "place", "tree", "under", "grass", "price"] 

list_a = list(filter(lambda x: x if ('a' not in x) else None,list_a))

print(list_a)