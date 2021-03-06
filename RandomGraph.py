# Random Graph Implementation Part 1: Jayon Huh, Catherine Tan, Wesley Yao
import random
import Queue
import pylab as pl
import numpy as np
import timeit


def graphExec():

	start = timeit.default_timer()


	# value of the number of nodes in our random graph
	n = 1000

	# p is the probablility of whether the edge exists
	p = 0.00

	# the number of times this is going to run
	k = 500

	# initialize the array of size nxn
	randomGraph = [[0 for x in xrange(n)] for x in xrange(n)] 

	# used to store number of connected components
	numComps = [0] * k

	# storing standard deviation for every value of p
	stdArray = [0] * 51

	# storing mean for every value of p
	meanArray = [0] * 51

	# array of p
	pArray = [0] * 51

	# loop through values of p.
	for prob in xrange(0, 51):

		# initialize value of p
		p = prob/50.00

		pArray[prob] = p

		# loop k times to get many samples
		for samples in xrange(0, k):
		
			# Go through the newly initialized random graph
			for x in xrange(0, n):

				for y in xrange(x, n): 

					# there will be no self edges.
					if x == y:
						randomGraph[x][y] = 0

					# give every possible edge a random value
					else:
						# generate a uniform random number between p and 1
						randomNumber = 0.00
						randomNumber = random.uniform(0, 1)

						# check if the random number generated is less than our p
						# if it is less than p then there is no edge at current relation
						if randomNumber >= p:

							randomGraph[x][y] = 0

						# if random number is greater than p, then that number becomes the relation's weight
						else:
							randomGraph[x][y] = randomNumber

			#print p
			#print randomGraph
			numComps[samples] = connectedComps(randomGraph, n)

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

	#pArray.reverse()

	#print pArray
	#print meanArray

	#meanArray.reverse()

	pl.plot(pArray, stdArray)

	pl.show()

	stop = timeit.default_timer()

	print stop - start 







# function that finds the number of connected components based on an adj matrix
def connectedComps(randomGraph, n):

	components = 0

	q = Queue.Queue()

	visited = [False] * n

	visited[0] = True

	q.put(0)

	while q.empty() == False:

		temp = q.get()

		for neighbor in xrange(0, n):

			if neighbor != temp:
	
				if randomGraph[temp][neighbor] > 0:

					if visited[neighbor] == False:

						q.put(neighbor)
						visited[neighbor] = True


		if q.empty() == True:

			components += 1

			for i in xrange(0, n):

				if visited[i] == False:
					q.put(i)
					visited[i] = True
					break

	#print components
	return components












graphExec()








