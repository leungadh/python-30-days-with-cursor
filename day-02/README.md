## Central Limit Theorem Demonstration (Day 02)

This program visualizes the Central Limit Theorem (CLT) by:
- Drawing many samples from a non-normal (exponential) population
- Computing the sample means for different sample sizes
- Showing that as sample size increases, the distribution of sample means approaches a normal distribution, centered at the population mean with standard error σ/√n

### Files
- `central.py`: Main script that generates the plots and console output

### How to Run
Using `uv` (recommended):

```bash
uv run day-02/central.py
```

Or with Python directly:

```bash
python3 day-02/central.py
```

### What You’ll See
- Console output with the population mean and standard deviation (from an exponential distribution)
- A 1×3 figure comparing the distribution of sample means for different sample sizes (e.g., n=5, 30, 100)
- Overlaid normal curves using CLT predictions (mean ≈ population mean, standard error = σ/√n)

### Parameters (inside the script)
- `population_size`: number of data points in the synthetic population
- `sample_sizes`: list of sample sizes used to compute sample means
- `num_samples`: how many samples are drawn for each sample size

### Dependencies
The script uses standard scientific Python libraries:
- `numpy`
- `matplotlib`
- `scipy`

If you run with `uv run`, these will be resolved in the environment. Otherwise, install them manually:

```bash
pip install numpy matplotlib scipy
```

### Notes
- A GUI backend is required to display plots. If running in a headless environment, consider saving figures to files by replacing `plt.show()` with `plt.savefig("clt.png", dpi=150)` in the script.


