import math
from collections import Counter 
def decrypt(string,k):		
	res = ""
	for c in string:
		if 65<=ord(c)<=90:
			#Upper
			ind = ( ord(c)-65 + k ) % 26
			res+= chr(ind+65)
		elif 97<=ord(c)<=122:
			#Lower
			ind = ( ord(c)-97 + k ) % 26
			res+= chr(ind+97)
		else:
			#Special
			res += c		
	return res
def cross_ent(string):
	#Frequency of letters in the english alphabet
	weights= [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406,0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056,0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
	sum = 0
	freq = Counter(string)
	for i in freq:		
		if 65<=ord(i)<=90:	
			sum += freq[i]*math.log(weights[ord(i)-65])
		elif 97<=ord(i)<=122:
			sum += freq[i]*math.log(weights[ord(i)-97])	
	
	return (-1)*sum
if __name__ == '__main__':
	file_r = open("breakme.input0.txt","r")
	string = file_r.read();
	min  = cross_ent(decrypt(string,0))
	res = string
	for k in range(1,26):	
		cur_res = decrypt(string,k)
		cur_min  = cross_ent(cur_res)
		if cur_min <= min: 
			min = cur_min
			res = cur_res
	print(res)	
	file_r.close()	
	file_w = open("breakme.output0.txt","w")
	file_w.write(res)
	file_w.close();

