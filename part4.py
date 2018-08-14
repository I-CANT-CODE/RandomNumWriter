#random number generator made into class method
#add history member
import numpy
import queue
import datetime
import threading
import time

class NumberSim:
    history = queue.Queue(100)
    
    
    def __init__(self):
        self.count = 0
        self.recent_num = 0
        self.FILE = open('history_file.txt','w')
        self.FILE.close()
        
    def RandNumGen(self):
        num = numpy.random.choice(numpy.arange(1,6),p = [.5,.25,.15,.05,.05])
        self.recent_num = num
        time = str(datetime.datetime.now().time())
        #print(num)
        #if self.history.full():#if q is full then remove oldest item
            #self.history.get()
        self.history.put([num,time])#add number
        #print(num,time)


    def PrintHistory(self): #for testing purposes only
        while not self.history.empty():
            print(self.history.get())

    def Writer(self):
        self.FILE = open('history_file.txt','a')
        inst = self.history.get()
        self.FILE.write(str(inst[0]) + ' , '  + inst[1] +'\n' )

    def PrintQlen(self):
        print('current length of q',self.history.qsize())
        
    
        
        

# test the function:

numbersim = NumberSim()

while True:
    
    NumGenT = threading.Thread(target = numbersim.RandNumGen, args = ())
    NumGenT.start()

    WriteT = threading.Thread(target = numbersim.Writer, args = ())
    WriteT.start()

    numbersim.PrintQlen()

    
    


numbersim.PrintHistory() #ensure that only last 100 items were saved into q 



    
