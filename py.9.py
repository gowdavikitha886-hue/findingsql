import random

trials = 5
heads = 1

for _ in range(trials):
    if random.choice(["Heads", "Tails"]) == "Heads":
        heads += 1

probability = heads / trials

print("Number of Heads:", heads)
print("Estimated Probability of Heads:", probability)