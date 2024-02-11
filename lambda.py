#Lambda arguements:expression
add10= lambda x:x+10
print(add10(5))

mult=lambda x,y:x*y
print(mult(2,7))

point2D=[(1,2),(15,1),(5,-1),(10,4)]
point2D_sorted=sorted(point2D,key=lambda x:x[1])
print(point2D)
print(point2D_sorted)

#map(function,sequence)
a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
c=[x*2 for x in a]
print(list(c))

#filter(function,sequence)
a=[1,2,3,4,5,6]
b=filter(lambda x:x%2==0,a)
c=[x for x in a if x%2==0]
print(list(c))

#Reduce(function,sequence)
from functools import reduce
a=[1,2,3,4]
product_a=reduce(lambda x,y:x*y,a)
print(product_a)
