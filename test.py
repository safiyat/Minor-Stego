data1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

phase_shift = int(numpy.floor(theta*S2));
i=0
j=gap
vacant=[0]*phase_shift
while i < len(target_split):
	for a in vacant:
		data1.insert(j, a)
	print "New sample sequence: data1[", j-2, ":", j+phase_shift+2, "] : ", data1[j-2:j+phase_shift+2]
	j+=gap+phase_shift
	i+=1
	
	
"""
i=0
data1=[]
while i < 100:
	data1.append(i)
	i+=1

phase_shift = 5
gap = 10
i=0
j=gap
vacant=[-1]*phase_shift
while i < 8:
	for a in vacant:
		data1.insert(j, a)
	print "New sample sequence: data1[", j-2, ":", j+phase_shift+2, "] : ", data1[j-2:j+phase_shift+2]
	j+=gap+phase_shift
	i+=1

i=0
data2=[]
while i < 8:
	temp=[]
	j = -10
	while j > -15:
		temp.append(j*(i+1))
		j-=1
	data2.append(temp)
	i+=1

while len(data2):
	i = data1.index(-1)
	j = 0
	while j < len(data2[0]):
		data1[i] = data2[0][j]
		i+=1
		j+=1
	data2.pop(0)
"""
