import BB_packaging as BB
import numpy as np

actData = np.array(parseData('matlab/actuatorPosition.txt'))
MMData = np.array(parseData('matlab/MM.txt'))

def parseData(path):
	lines = []
	with open(path) as f:
		lines = f.readlines()

	actData = []
	for l in lines:
		lsplit = l.split()
		arr = []
		for ls in lsplit:
			arr.append(float(ls))
		actData.append(arr)

	return actData

def getOri(pos, curr):

	pos = np.array(pos)
	curr = np.array(curr)

	BM = np.matmul(BB.packageBB(pos,actData), MMData)

	b_des = np.matmul(curr, np.transpose(BM))

	return b_des/(3e-3)

if __name__ == "__main__":

	print( getOri( [[0.01],[0.01],[0.15]] , [2, 2, 2, 2, 2, 2, 2, 2, 2] ) )

