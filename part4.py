#random number generator made into class method
#add history member
import numpy
import queue
import datetime
import threading
import time
import random

class NumberSim:
    history = queue.Queue(100)
    
    
    def __init__(self):
        self.count = 0
        self.recent_num = 0
        self.FILE = open('history_file.txt','w')
        self.FILE.close()
        
    def RandNumGen(self):
        while True:
            num = numpy.random.choice(numpy.arange(1,6),p = [.5,.25,.15,.05,.05])
            self.recent_num = num
            ctime = str(datetime.datetime.now().time())
            
        #if self.history.full():#if q is full then remove oldest item
            #self.history.get()
            self.history.put([num,ctime])#add number
            time.sleep(.1)
        #print(num,time)


    def PrintHistory(self): #for testing purposes only
        while not self.history.empty():
            print(self.history.get())

    def Writer(self):
        while True: 
            self.FILE = open('history_file.txt','a')
            inst = self.history.get()
            self.FILE.write(str(inst[0]) + ' , '  + inst[1] +'\n' )
            time.sleep(0)
            print('len of q:{}'.format(self.history.qsize()))

    def PrintQlen(self):
        print('current length of q',self.history.qsize())
        
    
        
        

# test the function:

numbersim = NumberSim()

for i in range(5):
    NumGenT = threading.Thread(target = numbersim.RandNumGen, args = (), name = 't{}'.format(i))
    NumGenT.start()
    print('{} has launched'.format(NumGenT.name))


WriteT = threading.Thread(target = numbersim.Writer, args = (), name = 't_w')
WriteT.start()
print('{} has launched'.format(WriteT.name))





    
    


numbersim.PrintHistory() #ensure that only last 100 items were saved into q 



    
