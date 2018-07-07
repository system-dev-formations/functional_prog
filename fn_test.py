from fn import _
from fn.op import zipwith
from itertools import repeat

assert list(map(_ * 2, range(5))) == [0,2,4,6,8]
assert list(filter(_ < 10, [9,10,11])) == [9]
assert list(zipwith(_ + _)([0,1,2], repeat(10))) == [10,11,12]

print (_ + 2)