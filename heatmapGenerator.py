#!/usr/bin/python
import csv
from PIL import Image
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="the file from which the heatmap will be created", metavar="FILE", type="string")
parser.add_option("-o", "--output", dest="outFileName",
                  help="the file where the heatmap will be saved", metavar="FILE", type="string")
parser.add_option("-l", "--labels", type="int", dest="numberOfLabels",
                  help="the number of labels used at the dataset")
parser.add_option("-p", "--pixelsPerLabel", dest="pixelsPerLabel",
                  help="the width of each cell box", type="int", default=20)
(options, args) = parser.parse_args()

if (options.numberOfLabels != None):
	numberOfLabels = options.numberOfLabels;
else:
	print "Error: You must define number of labels"
	sys.exit(2)
	
sizePerLabelPixel = options.pixelsPerLabel;

if (options.filename!=None):
	filename = options.filename;
else:
	print "Error: No input file given as argument"
	sys.exit(2)
	
if (options.outFileName!=None):
	outFileName = options.outFileName;
else:
	print "Error: No input file given as argument"
	sys.exit(2)

# Read the CSV first
data = csv.reader(open(filename,"r"))

labels = {}
index = 0;
for line in data:
  labels[index] = line[len(line)-numberOfLabels:]
  index += 1
  

totalInstances = index;
  


#initialize table
appearances={}
for i in range(0,numberOfLabels):
  appearances[i]={}
  for j in range(0,numberOfLabels):
    appearances[i][j]=0;
	
# Collect data into appearences table
for instance in range(0,totalInstances):
    for label in range(0,numberOfLabels):
      if int(labels[instance][label]) == 1:
        for i in range (0, numberOfLabels):
          if (int(labels[instance][i]) == 1):
            appearances[label][i] += 1.;
         
for i in range(0,numberOfLabels):
  pyi = appearances[i][i];
  for j in range(0,numberOfLabels):
    if (not (pyi == 0)):
      appearances[i][j] /= pyi;
    else:
      appearances[i][j] = 0;
  appearances[i][i] = pyi/ totalInstances;

size = numberOfLabels * sizePerLabelPixel
output = Image.new("L",(size,size));

for labelx in range(0,numberOfLabels):
  for labely in range(0,numberOfLabels):
    pixelValue =  appearances[labelx][labely]*255;
    for i in range(labelx * sizePerLabelPixel, ( labelx + 1 ) * sizePerLabelPixel):
      for j in range(labely * sizePerLabelPixel, ( labely + 1 ) * sizePerLabelPixel):
        position = i,j
        output.putpixel(position,pixelValue);
        
# Rotate to be compatible with Jesse Read
output = output.transpose(Image.ROTATE_90)
output.save(outFileName,"BMP");
