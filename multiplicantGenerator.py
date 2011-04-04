#!/usr/bin/python
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--attributes", dest="numOfAttributes",
                  help="the number of bits to be used (as attributes)", type="int")
parser.add_option("-l", "--labels", dest="numOfLabels",
                  help="the number of labels of the generated file", type="int")
parser.add_option("-s", "--start", type="int", dest="startFrom",
                  help="the number from which we are going to start")
(options, args) = parser.parse_args()

if (options.numOfAttributes != None):
	numOfAttributes = options.numOfAttributes;
else:
	print "Error: You must define number of attributes"
	sys.exit(2)
	
if (options.numOfLabels != None):
	numOfLabels = options.numOfLabels;
else:
	print "Error: You must define number of labels"
	sys.exit(2)

if (options.startFrom != None):
	startFrom = options.startFrom;
else:
	print "Error: You must define number where multiplication will start"
	sys.exit(2)
	
	
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
	
		
