import numpy as np

class slotMachine:
	def __init__(self,p):
		self.p = p
		self.reward_history = []
		self.play_count = 0

	def get_reward(self):
		return np.random.binomial(1, self.p)