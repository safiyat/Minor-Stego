def wavopen(file):						#file => character string
	from scikits.audiolab import wavread
	import numpy
	data, fs, encoding = wavread(file)
	temp = data.tolist()
	data = temp
	del temp
	del encoding
	t = int(numpy.ceil(len(data) / fs))
	return data, fs, t


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
