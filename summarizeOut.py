#!/usr/bin/python
import os;
import matplotlib.pyplot as plt
import numpy as np
directory = "/home/miltiadis/Desktop/datasets/mlTestbeds/MlUCSacc"
files = os.listdir(directory);
measureSize = 1000;

measureSum = [];
measureMin = [];
measureMax = [];
for i in range(0, measureSize):
	measureSum.append(0.);
	measureMin.append (2.);
	measureMax.append(-1.);

for outputFile in files:
	filePointer = open(directory + "/" + outputFile,'r');
	content = filePointer.read().split();
	for i in range(0,measureSize) :
		measureSum[i] += float(content[i]);
		if float(content[i]) < measureMin[i]:
			measureMin[i] = float(content[i]);
		if float(content[i]) > measureMax[i]:
			measureMax[i] = float(content[i]);

for i in range(0, measureSize):
	measureSum[i] /= (len(files) * 1.) ;
	

#fig, ax = plt.subplot(1)
#ax.plot(range(0,measureSize), measureMax, label = "mean", color = "blue");
plt.plot(range(0,measureSize), measureSum, label = "Mean Accuracy", color = "black");
plt.fill_between(range(0,measureSize), measureMin, measureMax, facecolor='yellow', alpha = 0.2, label = "range")
plt.grid();
plt.xlabel('Iteration');
plt.ylabel('Accuracy %');
plt.legend(loc='lower right')
plt.title('$DGUCS$ Accuracy of $adder^{24}_7$')
plt.show();
