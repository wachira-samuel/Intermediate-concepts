The following are the Intermediate concepts of Python:
## Collections
    from collections import Counter
    a='aaaaabbbbccc'
    my_counter=Counter(a)
    print(my_counter.keys())

    from collections import namedtuple
    Point=namedtuple('Point','X,Y')
    pt=Point(3,-4)
    print(pt)

    from collections import OrderedDict
    ordered_dict=OrderedDict()
    ordered_dict['a']=1
    ordered_dict['b']=2
    ordered_dict['c']=3
    ordered_dict['d']=4
    print(ordered_dict)

    from collections import defaultdict
    d=defaultdict(int)
    d['a']=1
    d['b']=2
    d['c']=3
    print(d['b'])

    from collections import deque
    d=deque()
    d.append(1)
    d.extend([2,3,4,5])
    print(d)

## Exception and Errors

    #Exception and errors
    try:
    a=5/0
    except Exception as e:
    print(e)
    except TypeError as e:
    print(e)

    class ValueTooHighError(Exception):
    pass
    class ValueTooSmallError(Exception):
    def __int__(self,message,test_value):
        self.message=message
        self.value=value

    def test_value(x):
        if x>100:
            raise ValueTooHighError("value is too high")
        if x<5:
            raise ValueTooSmallError('value is small',x)
    try:
    False
    except ValueTooHighError as e:
    print(e)
    except ValueTooSmallError as e:
    print(e.message,e.value)
    
## Itertools
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

## JSON(JavaScript Object Notation)
    import json

    class User:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    user= User('Max',27)

    def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name,'age':o.age,o.__class__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')
    userJSON=json.dumps(user,default=encode_user)
    print(userJSON)

## Lambda
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


