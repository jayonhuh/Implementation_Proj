# Random Graph Implementation Part 1: Jayon Huh, Catherine Tan, Wesley Yao
import random
import Queue
import pylab as pl
import numpy as np

def main():
	# value of the number of nodes in our random graph
	n = 20 

	# p is the probablility of whether the edge exists
	p = 0.00

	# the number of times this is going to run
	k = 500

	# initialize the array of size nxn
	randomGraph = [[0 for x in xrange(n)] for x in xrange(n)] 

	# used to store number of connected components
	numComps = [0] * k

	# storing standard deviation for every value of p
	stdArray = [0] * 50

	# storing mean for every value of p
	meanArray = [0] * 50

	# array of p
	pArray = [0] * 50

	# loop through values of p.
	for prob in xrange(0, 51):

		# initialize value of p
		p = prob/50

		pArray[prob] = p

		# loop k times to get many samples
		for samples in xrange(0, k):
		
			# Go through the newly initialized random graph
			for x in xrange(1, n - 1):
				for y in xrange(x + 1, n): 

					# no edge between self
					if x == y:
						randomGraph[x][y] = 0

					# generate a uniform random number between p and 1
					randomNumber = random.uniform(0, 1)

					# check if the random number generated is less than our p
					# if it is less than p then there is no edge at current relation
					if randomNumber < p:
						randomGraph[x][y] = 0

					# if random number is greater than p, then that number becomes the relation's weight
					else:
						randomGraph[x][y] = randomNumber


			numComps[k] = connectedComps(randomGraph)

		# compute standard deviation and mean to store into arrrays

		# calculating mean
		mean = 0;
		for comps in xrange(0, k):
			mean += numComps[comps]

		mean = mean/k

		# calculating standard deviation
		std = 0;
		for comps in xrange(0, k):
			std += (numComps[comps] - mean)**2

		std = (std/k) ** 0.5

		# store in our arrays
		meanArray[prob] = mean
		stdArray[prob] = std

	# Plotting all of our results

	pl.plot(pArray, meanArray)

	pl.show()




# function that finds the number of connected components based on an adj matrix
def connectedComps(adjMatrix):

	# array of vertices
	marks[0] * n

	# number of components
	components = 0

	# queue that we are going to use
	q = Queue()

	# loop through each vertex in graph
	for i in xrange(0, n):

		# check if the mark is 0
		if marks[i] == 0:

			# if so, add 1 to the componenet and put i into queue
			components += 1
			q.put(i)
			marks[i] = components

		# while the queue is not empty
		while q.empty() == false:

			# push next element from queue
			temp = q.get()

			for j in xrange(0, n):

				if adjMatrix[i][j] > 0:

					if marks[j] == 0:

						q.put(j)

	return components











