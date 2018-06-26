import numpy as np

def find_currents_distance(curr1, curr2):
	a = np.array(curr1)
	b = np.array(curr2)

	return np.linalg.norm(a-b)