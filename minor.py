from functions import *
import numpy
from scikits.audiolab import Format, Sndfile
#1
data1, S1, T1 = wavopen("sounds/02aashiqui150-less.wav")		#Cover audio file
data2, S2, T2 = wavopen("sounds/02flute04-less.wav")		#Target audio file

theta = 0.08
if T1 < 3 * T2 / theta:
	print "Cover audio file length is insufficient!!! Please use an audio file atleast ", 3*T2/theta, " seconds in length."
	quit()

#2
target_split = splitArray(data2, S2, theta)

#3
gap_in_s = int(numpy.floor(T1*theta/T2))
gap = gap_in_s * S1
#phase_shift_in_s = int(numpy.floor(theta*S2/S1))
#phase_shift = phase_shift_in_s * S1;
phase_shift = int(numpy.floor(theta*S2));
i=0
j=gap
vacant=[-1]*phase_shift			#fill it up with -1
print "Length of data1 before phaseshift: ", len(data1)
while i < len(target_split):
	for a in vacant:
		data1.insert(j, a)
	print i, ". New sample sequence: data1[", j-2, ":", j+phase_shift+2, "] : ", data1[j-2:j+phase_shift+2]
	j+=gap+phase_shift
	i+=1

print "Length of data1 after phaseshift: ", len(data1)

#4
data1[0]=T1^theta
data1[1]=S2^theta
data1[2]=T2^theta
data1[3]=theta

#5
while len(target_split):
	i = data1.index(-1)
	j = 0
	while j < len(target_split[0]):
		data1[i] = target_split[0][j]
		i+=1
		j+=1
	target_split.pop(0)

#6
op=numpy.asarray(data1)
format = Format('wav')
f = Sndfile("sounds/stego_file.wav", 'w', format, 1, 11025)
f.write_frames(op)
f.close()
