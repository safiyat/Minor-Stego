from functions import *
import numpy
import os
from scikits.audiolab import Format, Sndfile

file1 = raw_input("Enter the cover audio file name: ")
file2 = raw_input("Enter the target audio file name: ")

temp1 = 'ffmpeg -v quiet -i ' + file1 + ' -ac 1 cover.wav'
temp2 = 'ffmpeg -v quiet -i ' + file2 + ' -ac 1 target.wav'
os.system(temp1)
os.system(temp2)

#1
data1, S1, T1 = wavopen('cover.wav')		#Cover audio file
data2, S2, T2 = wavopen('target.wav')		#Target audio file


theta = float(raw_input("Enter the value of theta: "))
if T1 < 3 * T2 / theta:
	print "Cover audio file length is insufficient!!! Please use an audio file atleast ", 3*T2/theta, " seconds in length."
	quit()

#2
target_split = splitArray(data2, S2, theta)

#3

gap_in_s = int(numpy.floor(T1*theta/T2))
gap = gap_in_s * S1

i=0
j=gap

print "Length of data1 before phaseshift: ", len(data1)
while len(target_split):
	data1[j:0] = target_split[0]
#	print "####################################################################"
#	print "New sample sequence: data1[", j-2, ":", j+len(target_split[0])+2, "] : ", data1[j-2:j+len(target_split[0])+2]
	j+=gap+len(target_split[0])
	target_split.pop(0)

print "Length of data1 after phaseshift: ", len(data1)
#4

data1[0]=T1^len(data1)
data1[1]=S2^len(data1)
data1[2]=T2^len(data1)
data1[3]=theta

#5
"""
while len(target_split):
	i = data1.index(-1)
	j = 0
	while j < len(target_split[0]):
		data1[i] = target_split[0][j]
		i+=1
		j+=1
	target_split.pop(0)
"""
#6
op=numpy.asarray(data1)
format = Format('wav')
f = Sndfile("stego_file.wav", 'w', format, 1, S1)
f.write_frames(op)
f.close()
