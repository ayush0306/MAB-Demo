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
history = [0, 0, 0]

def print_history(turn_number):
	print("Turn", turn_number+1, "\nREWARD HISTORY:")
	for i in range(n_slots):
		print("Slot", i+1, "\t\t", end='')
	print()

	max_count = 0
	for i in range(n_slots):
		max_count = max(max_count, slots[i].play_count)

	for j in range(max_count):
		for i in range(n_slots):
			if slots[i].play_count > j:
				print(slots[i].reward_history[j], "\t\t", end='')
			else:
				print("\t\t", end='')
		print()
		# print slot[j].reward_history[i] if exists else blank

	for i in range(n_slots-1):
		print("================", end='')
	print("======")
	for i in range(n_slots):
		print(history[i], "\t\t", end='')
	print()
	for i in range(n_slots-1):
		print("================", end='')
	print("======")

for i in range(n_turns):
	x = int(input("Which slot machine do you want to play?")) - 1
	while x not in range(n_slots):
		print("Enter valid slot machine number");
		x = int(input("Which slot machine do you want to play?")) - 1
	reward = slots[x].get_reward()
	print("\nYou got a reward of",reward)
	reward_history.append(reward)
	history[x] += reward
	total_reward += reward
	total_expected_reward += slots[x].p
	slots[x].reward_history.append(reward)
	slots[x].play_count += 1
	print_history(i)
	print("\n\n\n")

print("Your Total Reward is",total_reward)
# print("Your Expected Reward was", total_expected_reward)
print("The Best Arm to Play would have been", np.argmax(probs)+1)