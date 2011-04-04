#!/usr/bin/python
numOfPositions = 9


print "@relation 'identity"+str(numOfPositions)+"'"

for i in range(0,numOfPositions):
	print "@attribute attr"+str(i)+" {0,1}"

for i in range(0,numOfPositions):
	print "@attribute label"+str(i)+" {0,1}"

print '@data'

for i in range(pow(2,numOfPositions),pow(2,numOfPositions+1)):
	number = bin(i)
	number = number[len(number)-numOfPositions:];
	line="";
	for character in number:
		line+=","+character
		
	number = bin(i+3)
	number = number[len(number)-numOfPositions:];
	for character in number:
		line+=","+character
	line = line[1:]
	print line
	
		
