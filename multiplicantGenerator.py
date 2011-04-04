#!/usr/bin/python
numOfAttributes = 7
numOfLabels = 7
startFrom = 11

print "@relation 'identity"+str(numOfAttributes)+"'"

for i in range(0,numOfAttributes):
	print "@attribute attr"+str(i)+" {0,1}"

for i in range(0,numOfLabels):
	print "@attribute label"+str(i)+" {0,1}"

print '@data'

for i in range(pow(2,numOfAttributes),pow(2,numOfAttributes+1)):
	number = bin(i)[3:];
	line="";
	for character in number:
		line+=","+character
  
	for j in range(startFrom,numOfLabels+startFrom):
		number = i - pow(2,numOfAttributes);
		if (number % j == 0):
			line += ",1"
		else:
			line += ",0"
	
	line = line[1:]
	print line
	
		
