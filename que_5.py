'''question 5'''

frozen_set_1 = frozenset(['A','B','C','D'])
frozen_set_2 = frozenset(['A',2,'C',4])
frozenset_union = frozen_set_1.union(frozen_set_2)
frozenset_common = frozen_set_1.intersection(frozen_set_2)
forzenset_difference = frozen_set_1.difference(frozen_set_2)
frozenset_distinct = frozenset_union.difference(frozenset_common)

print('frozen_set_1:',frozen_set_1,'\n')
print('frozen_set_2:',frozen_set_2,'\n')
print('frozenset_union:',frozenset_union,'\n')
print('frozenset_common:',frozenset_common,'\n')
print('forzenset_difference:',forzenset_difference,'\n')
print('frozenset_distinct',frozenset_distinct,'\n')