#!/usr/bin/python
import sys
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-l", "--labels", type="int", dest="numberOfLabels",
                  help="the number of labels used at the dataset")
                  
parser.add_option("-k", "--add", type="int", dest="addition", default=3,
                  help="the number to add to the problem")

(options, args) = parser.parse_args()

if (options.numberOfLabels != None):
	numOfPositions = options.numberOfLabels;
else:
	print "Error: You must define number of labels"
	sys.exit(2)

adder = options.addition;


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
		
	number = bin(i+adder) #TODO: Parametrize
	number = number[len(number)-numOfPositions:];
	for character in number:
		line+=","+character
	line = line[1:]
	print line
	
		
