import numpy
import os
from scikits.audiolab import Format, Sndfile

def wavopen(file):						#file => character string
	from scikits.audiolab import wavread
	import numpy
	data, fs, encoding = wavread(file)
	temp = data.tolist()
	data = temp
	del temp
	t = int(numpy.ceil(len(data) / fs))
	return data, fs, t, encoding


def splitArray(data, fs, theta):			#data => sampled data; fs => sampling frequency
	import numpy
	i=0
	splitA=[]
	length=int(numpy.floor(fs*theta))
	while i < len(data):
		a=i
		b=length+a
		splitA.append(data[a:b])
		i=b
	
	return splitA




def openFile(file):
	command = 'ffmpeg -y -i ' + file + ' -ac 1 temp.wav'
	os.system(str(command))
	data, S, T, en = wavopen('temp.wav')
	return data, S, T, en


def steg(data1, S1, T1, data2, S2, T2, theta):
	d1count = len(data1)
	d2count = len(data2)
	expectedcount = d1count + d2count
	target_split = splitArray(data2, S2, theta)
	gap_in_s = int(numpy.floor(T1*theta/T2))
	gap = gap_in_s * S1
	i=0
	j=gap
	while len(target_split):
		data1[j:0] = target_split[0]
#		print "####################################################################"
#		print "New sample sequence: data1[", j-2, ":", j+len(target_split[0])+2, "] : ", data1[j-2:j+len(target_split[0])+2]
		j+=gap+len(target_split[0])
		target_split.pop(0)

	data1[0]=T1^len(data1)
	data1[1]=S2^len(data1)
	data1[2]=T2^len(data1)
	data1[3]=theta

	size = len(data1)
#	print "\td1: ", d1count, "\n\td2: ", d2count, "\n\tec: ", expectedcount, "\n\tsize: ", size
	op = numpy.asarray(data1)
	format = Format('wav')
	f = Sndfile("stego_file.wav", 'w', format, 1, S1)
	f.write_frames(op)
	f.close()
	return size