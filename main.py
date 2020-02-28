import bandits
import numpy as np

np.random.seed()

n_slots = 3
n_turns = 15

probs = np.random.random(n_slots)
slots = []

for i in range(n_slots):
	slots.append(bandits.slotMachine(probs[i]))

total_reward = 0
total_expected_reward = 0
reward_history = []

for i in range(n_turns):
	x = int(input("Which slot machine do you want to play?")) - 1
	reward = slots[x].get_reward()
	print("You got a reward of ",reward)
	reward_history.append(reward)
	total_reward += reward
	total_expected_reward += slots[x].p

print("Your Total Reward is ",total_reward)
print("Your Expected Reward was", total_expected_reward)
print("The Best Arm to Play would be ", np.argmax(probs)+1)