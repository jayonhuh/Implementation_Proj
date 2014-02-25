# Random Graph Implementation Part 1

import random

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

# loop through values of p.
for prob in xrange(0, 51):

	# initialize value of p
	p = prob/50

	# loop k times to get many samples
	for samples in xrange(0, k):
	
		# Go through the newly initialized random graph
		for x in xrange(1, n - 1):
			for y in xrange(i + 1, n): 

				# no edge between self
				if i = j:
					randomGraph[i][j] = 0

				# generate a uniform random number between p and 1
				randomNumber = random.uniform(0, 1)

				# check if the random number generated is less than our p
				# if it is less than p then there is no edge at current relation
				if randomNumber < p:
					randomGraph[i][j] = 0

				# if random number is greater than p, then that number becomes the relation's weight
				else:
					randomGraph[i][j] = randomNumber


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

	std = std/k

	# store in our arrays
	meanArray[samples] = mean
	stdArray[samples] = std



# function that finds the number of connected components based on an adj matrix
def connectedComps(adjMatrix):

	return num









