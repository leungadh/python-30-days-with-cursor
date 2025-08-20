# Temperature Converter CLI

A command-line temperature converter that converts between Celsius, Fahrenheit, and Kelvin scales with input validation and configurable precision.

## Program Function

The temperature converter CLI tool allows users to convert temperatures between three temperature scales:
- **Celsius (°C)** - Metric temperature scale
- **Fahrenheit (°F)** - Imperial temperature scale  
- **Kelvin (K)** - Absolute temperature scale

Users can specify an input temperature in any scale and convert it to any other scale using command-line arguments.

## Program Logic

### Core Architecture

The program follows a modular design with clear separation of concerns:

1. **Conversion Functions**: Pure mathematical functions for each conversion path
2. **Main Convert Function**: Central logic that routes conversions and validates inputs
3. **CLI Parser**: Handles command-line argument parsing and validation
4. **Main Function**: Orchestrates the conversion process and handles errors

### Conversion Logic Flow

```
Input Validation → Scale Detection → Physical Validation → Conversion → Output Formatting
```

1. **Input Validation**: Ensures valid numeric input and proper scale specification
2. **Scale Detection**: Determines source and target temperature scales
3. **Physical Validation**: Checks for physically impossible temperatures (below absolute zero)
4. **Conversion**: Applies appropriate mathematical formula based on scale combination
5. **Output Formatting**: Rounds result to specified precision and displays

### Mathematical Formulas

The program implements standard temperature conversion formulas:

- **Celsius to Fahrenheit**: `F = (C × 9/5) + 32`
- **Fahrenheit to Celsius**: `C = (F - 32) × 5/9`
- **Celsius to Kelvin**: `K = C + 273.15`
- **Kelvin to Celsius**: `C = K - 273.15`
- **Fahrenheit to Kelvin**: `K = (F - 32) × 5/9 + 273.15`
- **Kelvin to Fahrenheit**: `F = (K - 273.15) × 9/5 + 32`

### Input Validation Logic

The program validates inputs at multiple levels:

1. **Scale Validation**: Ensures input and output scales are valid (c, f, k)
2. **Physical Validation**: Prevents temperatures below absolute zero:
   - Celsius: ≥ -273.15°C
   - Fahrenheit: ≥ -459.67°F  
   - Kelvin: ≥ 0K
3. **Type Validation**: Ensures numeric input values

### Error Handling Strategy

The program uses a custom `ConversionError` exception class to handle:
- Invalid temperature scales
- Physically impossible temperatures
- Unsupported conversion paths

Errors are displayed to stderr with descriptive messages, and the program exits with appropriate error codes.

## Usage

### Basic Syntax
```bash
python temp_converter.py --to <target_scale> --<input_scale> <temperature> [--precision <decimals>]
```

### Examples

**Convert Celsius to Fahrenheit:**
```bash
python temp_converter.py --to f --c 22
# Output: 71.6
```

**Convert Fahrenheit to Celsius:**
```bash
python temp_converter.py --to c --f 80
# Output: 26.67
```

**Convert Celsius to Kelvin with high precision:**
```bash
python temp_converter.py --to k --c 25 --precision 3
# Output: 298.15
```

### Command Line Arguments

| Argument | Description | Required | Default |
|----------|-------------|----------|---------|
| `--to` | Target scale (c, f, k) | Yes | - |
| `--c` | Input temperature in Celsius | One required | - |
| `--f` | Input temperature in Fahrenheit | One required | - |
| `--k` | Input temperature in Kelvin | One required | - |
| `--precision` | Decimal places for output | No | 2 |

## Technical Implementation

### Key Functions

- `c_to_f(c: float) -> float`: Celsius to Fahrenheit conversion
- `f_to_c(f: float) -> float`: Fahrenheit to Celsius conversion
- `c_to_k(c: float) -> float`: Celsius to Kelvin conversion
- `k_to_c(k: float) -> float`: Kelvin to Celsius conversion
- `f_to_k(f: float) -> float`: Fahrenheit to Kelvin conversion
- `k_to_f(k: float) -> float`: Kelvin to Fahrenheit conversion
- `convert(value: float, from_scale: str, to_scale: str) -> float`: Main conversion function

### Data Structures

- **VALID_SCALES**: Set containing valid scale identifiers
- **ConversionError**: Custom exception class for conversion-related errors

### Control Flow

1. **Argument Parsing**: Uses `argparse` to handle CLI arguments
2. **Input Processing**: Determines input value and scale from arguments
3. **Conversion Execution**: Calls main convert function with validation
4. **Output Generation**: Formats and displays result with specified precision
5. **Error Handling**: Catches and displays conversion errors appropriately

## Requirements

- Python 3.6+ (uses `__future__.annotations`)
- No external dependencies (uses only standard library)

## Error Codes

- **0**: Successful conversion
- **2**: Conversion error (invalid input, physical impossibility, etc.)

## Design Principles

- **Single Responsibility**: Each function has one clear purpose
- **Input Validation**: Comprehensive validation at multiple levels
- **Error Handling**: Graceful error handling with informative messages
- **Modularity**: Clean separation between conversion logic and CLI interface
- **Extensibility**: Easy to add new conversion paths or validation rules