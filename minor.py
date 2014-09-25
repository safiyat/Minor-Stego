from functions import *
import numpy
import os
from scikits.audiolab import Format, Sndfile

file1 = raw_input("Enter the cover audio file name: ")
file2 = raw_input("Enter the target audio file name: ")

fs = int(raw_input("Enter the desired sampling rate: "))

temp1 = 'ffmpeg -v quiet -i ' + file1 + ' -ac 1 -ar ' + str(fs) + ' cover.wav'
temp2 = 'ffmpeg -v quiet -i ' + file2 + ' -ac 1 -ar ' + str(fs) + ' target.wav'
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

#3 #5
gap_in_s = int(numpy.floor(T1*theta/T2))
gap = gap_in_s * S1

i=0
j=gap


while len(target_split):
	data1[j:0] = target_split[0]
	j+=gap+len(target_split[0])
	target_split.pop(0)

#4

data1[0]=T1^len(data1)
data1[1]=S2^len(data1)
data1[2]=T2^len(data1)
data1[3]=theta

#6
op=numpy.asarray(data1)
format = Format('wav')
f = Sndfile("stego_file.wav", 'w', format, 1, fs)
f.write_frames(op)
f.close()
