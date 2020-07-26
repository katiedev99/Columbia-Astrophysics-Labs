import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
#from astropy.timeseries import LombScargle

file = 'sco974gm.txt'
#file = raw_input("Filename: ")
with open(file) as f:
	reader = csv.reader(f)
	data = list(reader)

header = data[0]
index = 0
julianDate = []
VC = []
jdAverage = []
magAverage = []

for x in range(1, len(data)-2):
	line = data[x]
	index = index+1
	julianDate.append(float(line[1]))
	VC.append(float(line[2]))

def plotLightCurve(time, mag):
	plt.plot(time, mag)
	plt.xlabel("Julian Date")
	plt.ylabel("Variable - Comparison")
	#plt.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
	plt.show()

def periodogram(time, mag):
	print("bitch")
	t, m = LombScargle(time, mag).autopower()
	plt.plot(t, m)
	plt.show()

def averagePoints(time, mag, x):
	if x == 2:
		for x in range(0, len(time)-1, 2):
			y = x+1
			a = time[x]
			ax = time[y]
			aAvg = (a + ax) / 2
			jdAverage.append(aAvg)
			b = mag[x]
			bx = mag[y]
			bAvg = (b + bx) / 2
			magAverage.append(bAvg)
	if x == 3:
		for x in range(0, len(time)-2, 3):
			y = x+1
			z = x+2
			a = time[x]
			ax = time[y]
			az = time[z]
			aAvg = (a + ax + az) / 3
			jdAverage.append(aAvg)
			b = mag[x]
			bx = mag[y]
			bz = mag[z]
			bAvg = (b + bx + bz) / 3
			magAverage.append(bAvg)

#av = raw_input("Average data 2x or 3x? (2/3/N): ")
av = "N"

if av == "2":
	averagePoints(julianDate, VC, 2)
	plotLightCurve(jdAverage, magAverage)
elif av == "3":
	averagePoints(julianDate, VC, 3)
	plotLightCurve(jdAverage, magAverage)
else:
	av3 = raw_input("Average data 3x? (Y/N): ")
	if av3 == "Y":
		averagePoints(julianDate, VC, 3)
		plotLightCurve(jdAverage, magAverage)
	else:
		print("Plotting all data...")
		plotLightCurve(julianDate, VC)

#lightcurve = Lightcurve(julianDate, VC, input_counts=False)
#3print(lightcurve)

"""
Fourier Analysis:
 One can represent any recurring process as the combination of pure sine
 and cosine waves -- if one picks the right amplitudes and frequencies. The term
 "Fourier analysis" covers the many methods which shoot for this goal. There are
 many varieties: Fast Fourier Transforms (FFTs), and Discrete Fourier Transforms,
 to name just two. The basic idea is to convolve the observations with a set of
 pure sine and cosine waves and note the frequencies which produce a large result.
"""
