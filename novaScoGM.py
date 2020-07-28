import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

file1 = 'sco017be.txt'
meanmag1 = 15.30

values = ['17', '01', '28.15',
		'-43', '06', '12',
		'07', '04', '2020',
		'12', '0', '0']

file2 ='sco018be.txt'
meanmag2 = 15.29
file3 = 'sco019be.txt'
meanmag3 = 15.42
file4 = 'sco020be.txt'
meanmag4 = 15.35

files = [file1, file2, file3, file4]
fullJDs = []
fullMags = []

def averagePoints(time, mag, x):
		if (x == '2'):
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
		if (x == '3'):
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
		if (x == '4'):
			for x in range(0, len(time)-3, 4):
				w = x+1
				y = x+2
				z = x+3
				a = time[x]
				b = time[w]
				c = time[y]
				d = time[z]
				aAvg = (a + b + c + d) / 4
				jdAverage.append(aAvg)
				e = mag[x]
				f = mag[w]
				g = mag[y]
				h = mag[z]
				bAvg = (e+f+g+h) / 4
				magAverage.append(bAvg)

for element in files:
	with open(element) as f:
		reader = csv.reader(f)
		data = list(reader)

	julianDate = []
	jdAverage = []

	VC = []
	magAverage = []

	for x in range(1, len(data)-10):
		line = data[x]
		split_line = [i.split() for i in line]
		split_line = split_line[0]
		julianDate.append(float(split_line[0]))
		VC.append(float(split_line[1]))

	jd_extracted = list(julianDate)
	mag_extracted = list(VC)

	def removeEclipse(time, mag):
		for x in range(0, len(time)):
			if (float(time[x]) > 9017.47) and (float(time[x]) < 9017.54):
				jd_extracted.remove(time[x])
				mag_extracted.remove(mag[x])
			if (float(time[x]) > 9018.55) and (float(time[x]) < 9018.59):
				jd_extracted.remove(time[x])
				mag_extracted.remove(mag[x])

	def plotLightCurve(time, mag):
		plt.plot(time, mag)
		plt.xlabel("Julian Date")
		plt.ylabel("Variable - Comparison")
		plt.title(element)
		plt.show()


	ecl = 'Y'
	#raw_input("Remove Eclipse? (Y/N): ")
	if (ecl == "Y"):
		removeEclipse(julianDate, VC)
		plotLightCurve(jd_extracted, mag_extracted)
		for element in jd_extracted:
			fullJDs.append(element)
		for element in mag_extracted:
			fullMags.append(element)
	else:
		plotLightCurve(julianDate, VC)

av = raw_input("Average data 2x, 3x or 4x? (2/3/4/N): ")
if (av != "N"):
	averagePoints(fullJDs, fullMags, av)
	element = "Avg 4x " + str(file1[:-6]) + " + " + str(file2[:-6]) + " + " + str(file3[:-6]) + " " + str(file4[:-6])
	plotLightCurve(jdAverage, magAverage)

element = str(file1[:-4]) + " + " + str(file2[:-4]) + " + " + str(file3[:-4]) + " " + str(file4[:-4])
plotLightCurve(fullJDs, fullMags)

f = np.linspace(0.001, 100)
pgram = signal.lombscargle(fullJDs, fullMags, f, normalize = True)
plt.plot(f, pgram)
plt.xlabel('Period (days)')
plt.ylabel('Lomb-Scargle Power')
plt.title('Lomb-Scargle Graph with combined lightcurves & Eclipses removed')
plt.show()
