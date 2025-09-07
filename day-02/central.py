"""
Central Limit Theorem (CLT) demonstration

This script simulates drawing many samples from a clearly non-normal population
(exponential) and visualizes how the distribution of sample means approaches a
normal distribution as the sample size increases.

Key CLT expectations shown:
- Sample means are approximately normal even if the population is not
- Mean of sample means ≈ population mean
- Standard error decreases with larger sample sizes (σ / sqrt(n))
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

print("🚀 Let's verify the Central Limit Theorem together!")
print("We'll see how sample means become normally distributed even from skewed data.\n")

# --- Experiment parameters ---
population_size = 100000
sample_sizes = [5, 30, 100]  # Different sample sizes to demonstrate CLT
num_samples = 1000           # Number of samples to draw for each sample size

# Create a deliberately non-normal population (exponential is right-skewed)
population = np.random.exponential(scale=2, size=population_size)
pop_mean = np.mean(population)
pop_std = np.std(population)

print(f"📊 Population parameters (Exponential Distribution):")
print(f"   Mean = {pop_mean:.2f}, Std Dev = {pop_std:.2f}\n")

# Set up a 1x3 subplot to compare sample size effects side-by-side
plt.figure(figsize=(15, 5))
plt.suptitle("Central Limit Theorem Demonstration\nSample Means Approach Normality", fontsize=16)

for i, n in enumerate(sample_sizes):
    # Draw many samples of size n and compute each sample's mean
    sample_means = [np.mean(np.random.choice(population, size=n)) for _ in range(num_samples)]
    
    # Theoretical parameters predicted by CLT for sample means
    theoretical_mean = pop_mean
    theoretical_std = pop_std / np.sqrt(n)
    
    # Plot the empirical distribution of sample means
    plt.subplot(1, 3, i+1)
    plt.hist(sample_means, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    
    # Overlay corresponding normal curve with CLT mean and standard error
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    plt.plot(x, norm.pdf(x, theoretical_mean, theoretical_std), 'r-', linewidth=2)
    
    plt.title(f'Sample Size = {n}\nSE = {theoretical_std:.2f}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    
    # Visual cues for the CLT-predicted center and spread
    plt.axvline(theoretical_mean, color='k', linestyle='dashed', linewidth=1)
    plt.text(0.05, 0.8, f'μ = {theoretical_mean:.2f}\nσ = {theoretical_std:.2f}', 
             transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

print("\n🎉 CLT Verification Complete!")
print("Key observations:")
print("1. Even though the original population is skewed (exponential),")
print("2. The distribution of sample means becomes more normal as sample size increases")
print("3. The standard error (SE) decreases with larger sample sizes")
print("4. The mean of sample means matches the population mean")
print("\n💡 Remember: CLT is why many statistical methods work even with non-normal data!")