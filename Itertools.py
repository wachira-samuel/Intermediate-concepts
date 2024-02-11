from itertools import product
a=[1,2]
b=[3,4]
prod=product(a,b,)
print(list(prod))

from itertools import permutations
a=[1,2,3]
perm=permutations(a)
print(list(perm))

from itertools import combinations_with_replacement
a=[1,2,3,4]
comb_wr=combinations_with_replacement(a,2)
print(list(comb_wr))

from itertools import accumulate
a=[1,2,3,4]
acc=accumulate(a)
print(a)
print(list(acc))

from itertools import groupby
def smaller_than_3(x):
    return x<3
a=[1,2,3,4]
group_obj=groupby(a,lambda x:x<3)
for key,value in group_obj:
    print(key,list(value))

from itertools import count
for i in count(10):
    print(i)
    if i==15:
        break
