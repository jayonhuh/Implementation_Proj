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
	k = 200

	# initialize the array of size nxn
	randomGraph = [[0 for x in xrange(n)] for x in xrange(n)] 

	# used to store number of connected components
	numComps = [0] * k

	# storing our avg MST weight
	mstWeightArray = [0] * 51

	# array of p
	pArray = [0] * 51

	# loop through values of p.
	for prob in xrange(0, 51):

		# initialize value of p
		p = prob/50.00

		pArray[prob] = p

		MSTWeightSampleSum = 0.0000000000

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
							randomGraph[y][x] = 0

						# if random number is greater than p, then that number becomes the relation's weight
						else:
							randomGraph[x][y] = randomNumber
							randomGraph[y][x] = randomNumber

			# here we have a newly created random graph. We find the connected components
			newMarks = connectedComps(randomGraph, n)

			# with this array, we create smaller adjacency matrices to represent our connected components
			numConnectedComponents = max(newMarks)

			#print max(newMarks)

			# this variable will contain the average MST weight of this graph
			avgMSTWeightForOneGraph = 0.000000000000000

			# loop through each connected component
			for i in xrange(1, numConnectedComponents + 1):

				# create a temp array to store the adj matrix for our connected component
				connectedComponentNodes = []

				# go through our array that tells us which nodes are part of which connected component
				for j in xrange(0, n):

					# if the selected node is part of the ith connected component...
					if(newMarks[j] == i):

						# then add it into our temporary array
						connectedComponentNodes.append(j)

				# at this point, we have a list with nodes pertaining to a single connected component

				# find the size of our connected component
				newConnectedComponentSize = len(connectedComponentNodes)

				#print newConnectedComponentSize

				# check the size because the MST weight will be 0

				if(newConnectedComponentSize == 1):

					# weight of this connected component will be 0
					avgMSTWeightForOneGraph = avgMSTWeightForOneGraph

				# otherwise, we must find the weight of the MST
				else:

					# new adjacency matrix for our connected component
					adjMatrixConComp = [[0 for x in xrange(newConnectedComponentSize)] for x in xrange(newConnectedComponentSize)]

					# loop through this adjacency matrix to fill it in.
					for x in xrange(0, newConnectedComponentSize):

						for y in xrange(0, newConnectedComponentSize):

							# construct the adjency matrix
							adjMatrixConComp[x][y] = randomGraph[connectedComponentNodes[x]][connectedComponentNodes[y]]

					# at this point, find the MST of our newly created adjacency matrix.

					MSTEdges = Prim(adjMatrixConComp)

					# variable to store the weights of each edge
					edgeSum = 0.00000000000000

					# loop through the given edges to find the MST weight of this connected component

					for x in xrange(0, len(MSTEdges)):

						edgeSum = edgeSum + adjMatrixConComp[MSTEdges[x][0]][MSTEdges[x][1]]
						#print edgeSum

					# just add our edgeSum to our weight
					avgMSTWeightForOneGraph = avgMSTWeightForOneGraph + edgeSum

				#print numConnectedComponents

				# calculate the avg MST weight for this graph
				avgMSTWeightForOneGraph = avgMSTWeightForOneGraph/numConnectedComponents

			# sum of all samples
			MSTWeightSampleSum = MSTWeightSampleSum + avgMSTWeightForOneGraph

		MSTWeightSampleSum = MSTWeightSampleSum/k

		# store our MSTweight for this probability
		mstWeightArray[prob] = MSTWeightSampleSum


	pl.plot(pArray, mstWeightArray)

	pl.show()

	stop = timeit.default_timer()

	print stop - start  







# function that finds the number of connected components based on an adj matrix
def connectedComps(randomGraph, n):

	components = 1

	q = Queue.Queue()

	marks = [0] * n

	marks[0] = 1

	q.put(0)

	while q.empty() == False:

		temp = q.get()

		for neighbor in xrange(0, n):

			if neighbor != temp:
	
				if randomGraph[temp][neighbor] > 0:

					if marks[neighbor] == 0:

						q.put(neighbor)
						marks[neighbor] = components
						


		if q.empty() == True:

			components += 1

			for i in xrange(0, n):

				if marks[i] == 0:
					q.put(i)
					marks[i] = components
					break

	# return marks
	return marks




# thanks nicolagreco of github for this
def Prim (Adj):

	T = []
	n = len(Adj)
	Nearest = []
	MinDist = []

	for i in range(0,n):
		Nearest.append(0)
		MinDist.append(0)

	for i in range(1, n):

		Nearest[i] = 0
		MinDist[i] = Adj[i][0]

	for i in range(0, n-1):
		min = None
		for j in range(1, n):
			if ((min and MinDist[j] and 0 <= MinDist[j] < min) or (not min and  0 <= MinDist[j])):
				min = MinDist[j]
				k = j

		T.append((k, Nearest[k]))
		#print T

		MinDist[k] = -1
		MinDist[Nearest[k]] = -1

		for j in range(1, n):
			if ((MinDist[j] and Adj[k][j] and Adj[k][j] < MinDist[j]) or not MinDist[j] ):
				MinDist[j] = Adj[k][j]
				MinDist[k] = Adj[j][k]

				Nearest[j] = k
				Nearest[k] = j

	return T










	#print marks












graphExec()