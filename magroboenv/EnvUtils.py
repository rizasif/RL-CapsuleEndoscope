import numpy as np

def find_currents_distance(curr1, curr2):
	a = np.array(curr1)
	b = np.array(curr2)

	return np.linalg.norm(a-b)

def find_config_distance(config1, config2):
	a = np.array(config1)
	b = np.array(config2)

	return np.linalg.norm(a-b)

def calculate_reward(goal_config, slave_config, last_slave_config):
		num = find_config_distance(last_slave_config, slave_config)
		dnum = find_config_distance(goal_config, slave_config)

		print("Slave Dist: {} ; Last Dist: {}".format(num,dnum))

		percentage_error = 100.0* (num/dnum)
		print("Error={}%".format(percentage_error ))

		# if self.percentage_error > 100:
		#	 return -1
		# else:
		#	 return (1.0 - self.percentage_error/100)

		return percentage_error, (1.0 - percentage_error/10)