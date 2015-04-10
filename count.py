#!/usr/bin/python

import sys

def count(filename,word):
	counter = 0
	fopen = open(filename,'rU')
	string = fopen.read()
	fstring = string.split(' ')
	for i in fstring:
		if i == word:
			counter = counter + 1
			#print('You entered::> '+str(counter)+' times in file')
		#else:
			#print 'Word not found'
	print word + ' ' + str(counter) + ' times in file'

def main():
	#count(sys.argv[1],sys.argv[2])
	word = raw_input('Enter the word you want to count::>')
	count(sys.argv[1],word)
if __name__ == '__main__':
	main()
