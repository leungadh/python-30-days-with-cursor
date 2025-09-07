# Python 30 Days with Cursor

A collection of small projects built day-by-day.

## Day 01 — Temperature Converter CLI

Command-line tool to convert temperatures between Celsius, Fahrenheit, and Kelvin with input validation and configurable precision.

- Code: `day-01/temp_converter.py`
- Docs: `day-01/README.md`

Quick examples:

```bash
python day-01/temp_converter.py --to f --c 22        # 71.6
python day-01/temp_converter.py --to c --f 80        # 26.67
python day-01/temp_converter.py --to k --c 25 --precision 3  # 298.15
```

## Day 02 — Six-Dice Roller GUI (Histogram)

Interactive web page that simulates rolling six dice, animates the dice, computes the average per roll, and updates a histogram showing the distribution of average values.

- File: `day-02/dice_web.html`
- How to run: Open the HTML file directly in a web browser (no server needed).
- Features:
  - Roll six dice with animation
  - Track total rolls and average of averages
  - Histogram of average value ranges (1.0–6.0)

```text
Open: day-02/dice_web.html in your browser
Click: "Roll All Dice" to simulate a roll and update the histogram
```

