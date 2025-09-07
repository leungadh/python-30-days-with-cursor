## Central Limit Theorem Demonstration (Day 02)

This program visualizes the Central Limit Theorem (CLT) by:
- Drawing many samples from a non-normal (exponential) population
- Computing the sample means for different sample sizes
- Showing that as sample size increases, the distribution of sample means approaches a normal distribution, centered at the population mean with standard error σ/√n

### Files
- `central.py`: Main script that generates the plots and console output
- `dice.py`: Dice-based CLT demo (supports fair or biased dice)
- `dice_web.html`: Six-dice roller web page with histogram of average values

### How to Run (Python scripts)
Using `uv` (recommended):

```bash
uv run day-02/central.py
uv run day-02/dice.py
```

Or with Python directly:

```bash
python3 day-02/central.py
```

### What You’ll See (Python scripts)
- Console output with the population mean and standard deviation (from an exponential distribution)
- A 1×3 figure comparing the distribution of sample means for different sample sizes (e.g., n=5, 30, 100) in `central.py`
- Overlaid normal curves using CLT predictions (mean ≈ population mean, standard error = σ/√n)

### Dice CLT (dice.py)
- Simulates the average of many dice per trial and repeats for 30, 300, and 3000 trials
- Configurable number of dice (default: 100)
- Biased dice probabilities used by default:
  - P(1)=0.30, P(2)=0.10, P(3)=0.10, P(4)=0.10, P(5)=0.10, P(6)=0.30
- Shows three histograms with the CLT normal overlay (center = E[X], spread = sqrt(Var[X]/num_dice))

To switch to fair dice, set `probs=None` and sample with `np.random.randint(1, 7, size=(trials, num_dice))` instead of `np.random.choice`.

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

---

## Six-Dice Roller Web GUI (dice_web.html)

An interactive web page that simulates rolling six dice, animates each roll, computes the average of the six results, and updates a histogram showing the distribution of average values over time.

### How to Run
- Open `day-02/dice_web.html` directly in your web browser (no server required).

### Features
- Roll six dice with a single button
- Animated dice with dynamic pips
- Histogram of average value ranges (1.0–6.0), updated after each roll
- Live stats: total rolls, average of averages, most frequent average range

### Usage
1. Open the file in a browser
2. Click "Roll All Dice" to simulate a roll
3. Observe the dice animation, updated histogram bars, and stats

### Code Structure
- Pure HTML/CSS/JavaScript (no external dependencies)
- DOM-driven rendering for dice and histogram bars
- Simple scaling for histogram bar heights to improve visibility


