#!/usr/bin/python
import random
numOfVars = 2
numOfSamples = 400


print "@relation 'partition'"

for i in range(0,numOfVars):
	print "@attribute attr"+str(i)+" numeric"

for i in range(0,pow(2,numOfVars)):
	print "@attribute label"+str(i)+" {0,1}"

print '@data'

for i in range(1,numOfSamples):
	line = "";
	numbers = {}
	for k in range(0,numOfVars):		
		numbers[k] = random.normalvariate(0,5);
		line += "," + str(numbers[k])
	
	for k in range(pow(2,numOfVars),pow(2,numOfVars+1)):
		inequalities = bin(k)[3:];
		# Parse
		activated = True;
		for l in range(0,numOfVars):
			if ((inequalities[l] == "0" and numbers[l] > 0) or (inequalities[l] == "1" and numbers[l] < 0)):
				activated = False
			
		
		
		if activated:
			line += ",1"
		else:
			line += ",0"
		
	line = line[1:]
	print line
	
		
