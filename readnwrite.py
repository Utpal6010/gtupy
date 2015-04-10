#!/usr/bin/python
import sys

def readfile(file1,file2):
	fopen = open(file1,'rU')
	string = fopen.read()
	print string
	fwrite = open(file2,'w')
	string = fwrite.write('written')

def main():
	#print 'hi'
	readfile(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
	main()
