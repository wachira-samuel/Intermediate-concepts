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

