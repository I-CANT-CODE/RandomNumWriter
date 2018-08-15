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
    
    FLAG = False #flag used to check for keyboard interrupt so program ca terminate
    def __init__(self):
        
        
        self.FILE = open('history_file.txt','w') #open file to make it exist
        self.FILE.close()#close it
        
        
    def RandNumGen(self):
        while self.FLAG == False:
            num = numpy.random.choice(numpy.arange(1,6),p = [.5,.25,.15,.05,.05]) #generate num
            ctime = datetime.datetime.now().time() #save the current time stamp
            
            time.sleep(.5) # this is not necessary, but helps debug and clarify
            
            
            #print("{} {}\n".format(num,ctime))
            #if self.history.full():#if q is full then remove oldest item
            #self.history.get()
            #print(num,time)

            self.history.put([num,ctime])#add number and time to queue


    

    def Writer(self):
        while self.FLAG == False:
            self.FILE = open('history_file.txt','a') #open file for appending line
            inst = self.history.get() #get the most recent item in the history
            self.FILE.write('\n'+str(inst[0]) + ','  + str(inst[1])) #add the most recent item to the file
            
            #print('len of q:{}'.format(self.history.qsize()))

           
        

# test the function:

numbersim = NumberSim()
try:
    for i in range(5): #launch generation threads
        NumGenT = threading.Thread(target = numbersim.RandNumGen, args = (), name = 't{}'.format(i))
        NumGenT.start()
        print('{} has launched'.format(NumGenT.name))

    #launch writing threads
    WriteT = threading.Thread(target = numbersim.Writer, args = (), name = 't_w')
    WriteT.start()
    print('{} has launched'.format(WriteT.name))


#need this main loop to check for keyboard interrupt so program quits when hit "ctrl c"
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    numbersim.FLAG = True
    




    
    


    
