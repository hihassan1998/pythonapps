# MathOperations

A Python package providing basic mathematical operations and statistical functions.

## Functions

### `square(number)`

Returns the square of a given number.

#### Parameters:

- `number` (float): The input number.

#### Returns:

- `float`: The square of the input number.

### `double(number)`

Returns twice the value of a given number.

#### Parameters:

- `number` (float): The input number.

#### Returns:

- `float`: Twice the value of the input number.

### `add(a, b)`

Returns the sum of two given numbers.

#### Parameters:

- `a` (float): The first number.
- `b` (float): The second number.

#### Returns:

- `float`: The sum of the two input numbers.

### `mean(numbers)`

Returns the mean (average) of a given list of numbers.

#### Parameters:

- `numbers` (list): List of numbers.

#### Returns:

- `float`: The mean of the input list of numbers.

### `median(numbers)`

Returns the median of a given list of numbers.

#### Parameters:

- `numbers` (list): List of numbers.

#### Returns:

- `float`: The median of the input list of numbers.

## Usage:

```python
# Import the functions from the MathOperations package
from MathOperations.basic import square, double, add
from MathOperations.stats import mean, median

# Test the functions
number = 5
print(f"Square of {number}: {square(number)}")
print(f"Double of {number}: {double(number)}")

a, b = 3, 7
print(f"Sum of {a} and {b}: {add(a, b)}")

numbers_list = [1, 2, 3, 4, 5]
print(f"Mean of {numbers_list}: {mean(numbers_list)}")
print(f"Median of {numbers_list}: {median(numbers_list)}")

### Instructions for testing the app in python:

At the terminal type python3 to invoke python interpreter.
Once the python interpreter is loaded.
At the python prompt type import mymath
If the above command runs without errors, it is an indication that the mymath package is successfully loaded.
At the python prompt type mymath.basic.add(3,4)
You should see an output 7 on the screen.
At the python prompt type mymath.stats.mean([3,4,5])
You should see an output 4.0 on the screen.
Type exit() to quit python interpreter