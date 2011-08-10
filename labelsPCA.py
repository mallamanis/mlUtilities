#!/usr/bin/python
import csv
import numpy as np
import sys
from optparse import OptionParser
import matplotlib.mlab

parser = OptionParser()
parser.add_option("-i", "--input", dest="filename",
                  help="the file from which the heatmap will be created", metavar="FILE", type="string")
parser.add_option("-l", "--labels", type="int", dest="numberOfLabels",
                  help="the number of labels used at the dataset")
parser.add_option("-v", "--minVariance", dest="minVariance",
                  help="the minimum variance for PCA", type="float", default=0.05)
                  
(options, args) = parser.parse_args()

if (options.numberOfLabels != None):
	numberOfLabels = int(options.numberOfLabels);
else:
	print "Error: You must define number of labels"
	sys.exit(2)
	
	
if (options.filename!=None):
	filename = options.filename;
else:
	print "Error: No input file given as argument"
	sys.exit(2)

minVar = options.minVariance
	
# Read the CSV first
data = csv.reader(open(filename,"r"))

labels = []
attributes = []
index = 0;
startParsing = False;
for line in data:
	
	if (len(line)>0 and (len(line)-numberOfLabels)>0 and startParsing):
		labels.append (line[len(line)-numberOfLabels:])
		attributes.append (line[1: len(line)-numberOfLabels])
		index += 1
	if len(line)>0 and line[0]=="@data":
		startParsing = True

totalInstances = index;

# Convert to numeric values
for i in range(0,len(labels)):
	for j in range(0,len(labels[i])):
		labels[i][j] = int (labels[i][j])

for i in range(0,len(attributes)):
	for j in range(0,len(attributes[i])):
		attributes[i][j] = float (attributes[i][j])

labelArray = np.array(labels)
featureArray = np.array(attributes)
print featureArray

labelResult = matplotlib.mlab.prepca(labelArray,minVar)
attributeResult = matplotlib.mlab.prepca(featureArray, minVar)
print 'attributeSpace: ' 
print attributeResult
print 'labelSpace: ' 
print labelResult[2]


