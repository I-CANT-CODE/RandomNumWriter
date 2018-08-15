# program checker

#open written file
import datetime
FILE = open('history_file.txt','r')

line = FILE.readline()
iterations = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0

while line:
    line = FILE.readline()
    if line.find(',')!=-1:
        iterations = iterations +1
        items = line.split(',')
       #parse the line to get the number and the time in seconds
        number = items[0]
        time = items[1]
        time = time.split('\n')
        time = time[0]
        time = time.split(':')
        seconds = time[2]
        print(number)
        print(seconds)
        num = int(number)
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
            
print("number distributions --> 1:{}  2:{}  3:{}  4:{}  5:{}".format(ones/iterations,twos/iterations,threes/iterations,fours/iterations,fives/iterations,))
