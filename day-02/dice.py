"""
Central Limit Theorem via Dice Averages

Experiment:
- Roll many six-sided dice per trial (num_dice)
- For each trial, compute the average of those dice
- Repeat for 30, 300, and 3000 trials
- Plot histograms of the averages with CLT normal overlays

Note: The die is biased (not fair). Probabilities:
P(1)=0.30, P(2)=0.10, P(3)=0.10, P(4)=0.10, P(5)=0.10, P(6)=0.30.
Even with a non-uniform population, CLT predicts the mean of many dice
approaches a normal distribution with mean equal to E[X] and standard
deviation equal to sqrt(Var[X]/num_dice).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- Parameters ---
num_dice = 100
faces = np.arange(1, 7)  # die faces 1..6
# Biased probabilities: 1=30%, 2=10%, 3=10%, 4=10%, 5=10%, 6=30%
probs = np.array([0.30, 0.10, 0.10, 0.10, 0.10, 0.30])
trial_counts = [30, 300, 3000]

# Population properties for a single biased die X
# E[X] = sum(x * p_x), E[X^2] = sum(x^2 * p_x), Var[X] = E[X^2] - (E[X])^2
die_mean = float(np.dot(faces, probs))
e_x2 = float(np.dot(faces ** 2, probs))
die_var = e_x2 - die_mean ** 2

# For the average of num_dice dice:
# mean_avg = die_mean
# std_avg = sqrt(die_var / num_dice)
mean_avg = die_mean
std_avg = np.sqrt(die_var / num_dice)

fig = plt.figure(figsize=(15, 5))
plt.suptitle(
    f"CLT with Biased Dice: Averages of {num_dice} Dice\n"
    "P(1)=0.30, P(2..5)=0.10, P(6)=0.30",
    fontsize=16,
)

for i, trials in enumerate(trial_counts):
    # Simulate trials with biased probabilities: shape (trials, num_dice)
    # Each row contains one trial of num_dice outcomes
    rolls = np.random.choice(faces, size=(trials, num_dice), p=probs)
    # Compute average per trial (sampling distribution of the mean)
    averages = rolls.mean(axis=1)

    # Theoretical normal for the sampling distribution of the sample mean
    # For finite trials, overlay the normal centered at mean_avg with std_avg
    plt.subplot(1, 3, i + 1)
    plt.hist(averages, bins=30, density=True, alpha=0.7, color='orchid', edgecolor='black')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 200)
    plt.plot(x, norm.pdf(x, loc=mean_avg, scale=std_avg), 'r-', linewidth=2, label='CLT Normal')

    # Title shows the number of trials and the CLT-predicted center/spread
    plt.title(f"Trials = {trials}\nMean≈{mean_avg:.2f}, SD≈{std_avg:.2f}")
    plt.xlabel(f"Average of {num_dice} Dice")
    plt.ylabel("Density")
    plt.axvline(mean_avg, color='k', linestyle='dashed', linewidth=1)
    plt.legend()

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()

