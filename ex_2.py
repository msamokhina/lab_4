from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

res = [x for x in Unique(data1, False)]
print(res)

res = [x for x in Unique(list(data2), False)]
print(res)
