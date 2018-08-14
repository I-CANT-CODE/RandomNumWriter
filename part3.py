#random number generator made into class method
#add history member
import numpy
import queue

class NumberSim:
    history = queue.Queue(100)
    
    def __init__(self):
        self.count = 0
        self.recent_num = 0
    def RandNumGen(self):
        num = numpy.random.choice(numpy.arange(1,6),p = [.5,.25,.15,.05,.05])
        self.recent_num = num
        #print(num)
        if self.history.full():#if q is full then remove oldest item
            self.history.get()
        self.history.put([num,"null"])#add number


    def PrintHistory(self): #for testing purposes only
        while not self.history.empty():
            print(self.history.get())
        
        

# test the function:

numbersim = NumberSim()

for i in range(200): #run sim 200 times
    numbersim.RandNumGen()
    
numbersim.PrintHistory() #ensure that only last 100 items were saved into q 



    
