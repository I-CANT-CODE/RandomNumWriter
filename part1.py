#random number generator with distribution
import numpy

def RandNumGen():
    num = numpy.random.choice(numpy.arange(1,6),p = [.5,.25,.15,.05,.05])
    print(num)
    return num

# test the function:
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
for i in range(1000):
    num = RandNumGen()

    if num == 1:
        ones=ones+1
    elif num == 2:
        twos=twos+1
    elif num == 3:
        threes=threes+1
    elif num == 4:
        fours=fours+1
    elif num == 5:
        fives=fives+1


print("actual distribution:",ones/1000,' ', twos/1000,' ', threes/1000,' ', fours/1000,' ', fives/1000)
    
