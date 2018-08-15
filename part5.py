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
    
    FLAG = False
    def __init__(self):
        self.count = 0
        self.recent_num = 0
        self.FILE = open('history_file.txt','w')
        self.FILE.close()
        
        
    def RandNumGen(self):
        while self.FLAG == False:
            num = numpy.random.choice(numpy.arange(1,6),p = [.5,.25,.15,.05,.05])
            self.recent_num = num
            time.sleep(.5)
            ctime = datetime.datetime.now().time()
            #print("{} {}\n".format(num,ctime))
        #if self.history.full():#if q is full then remove oldest item
            #self.history.get()
            self.history.put([num,ctime])#add number
            
        #print(num,time)


    

    def Writer(self):
        while self.FLAG == False:
            self.FILE = open('history_file.txt','a')
            inst = self.history.get()
            self.FILE.write(str(inst[0]) + ' , '  + str(inst[1]) +'\n' )
            
            #print('len of q:{}'.format(self.history.qsize()))

           
        

# test the function:

numbersim = NumberSim()
try:
    for i in range(5):
        NumGenT = threading.Thread(target = numbersim.RandNumGen, args = (), name = 't{}'.format(i))
        NumGenT.start()
        print('{} has launched'.format(NumGenT.name))


    WriteT = threading.Thread(target = numbersim.Writer, args = (), name = 't_w')
    WriteT.start()
    print('{} has launched'.format(WriteT.name))
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    numbersim.FLAG = True
    




    
    


    
