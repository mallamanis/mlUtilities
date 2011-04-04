#!/usr/bin/python
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--labels", type="int", dest="numberOfLabels",
                  help="the number of labels used at the dataset")

(options, args) = parser.parse_args()

if (options.numberOfLabels != None):
	numOfPositions = options.numberOfLabels;
else:
	print "Error: You must define number of labels"
	sys.exit(2)



print "@relation 'position"+str(numOfPositions)+"'"

for i in range(0,numOfPositions):
	print "@attribute attr"+str(i)+" {0,1}"

for i in range(0,numOfPositions):
	print "@attribute label"+str(i)+" {0,1}"

print '@data'

for i in range(pow(2,numOfPositions),pow(2,numOfPositions+1)):
	number = bin(i)[3:];
	line="";
	for character in number:
		line+=","+character
	flag = 1;
	for character in number:
		if flag==1 and character=='1':
			line+=",1";
			flag = 0;
		else:
			line+=",0";
	line = line[1:]
	print line
	
		
