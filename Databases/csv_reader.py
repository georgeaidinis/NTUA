#coding=utf-8

import csv

def read_the_file(name):
	with open(name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		array = []
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				array.append(row)
				line_count += 1
		return array

def main():
	read_the_file("books.csv")

if __name__ == '__main__':
	main()
	
