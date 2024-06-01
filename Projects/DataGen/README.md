## DataGen: Library for Generating Random Data of Various Types

### Description

**DataGen** is a library for generating random data of various types. It provides simple and convenient methods for creating random strings, numbers, lists, and other data types.

### Key Features

- **Generation of Random Strings**: The library allows creating random strings of a specified length from ASCII characters.
- **Generation of Random Numbers**: You can generate random integers within a specified range or floating-point numbers with a given precision.
- **Generation of Random Lists**: DataGen can create random lists of a specified length containing numbers, strings, or other elements.
- **Support for Various Data Types**: The library supports generating data of various types, making it a versatile tool for testing and creating random data.

### Example Usage

```python
import datagen

# Generating a random string
random_string = datagen.generate_string(length=10)

# Generating a random integer within a range
random_int = datagen.generate_integer(min_value=0, max_value=100)

# Generating a random floating-point number
random_float = datagen.generate_float(min_value=0.0, max_value=1.0, precision=2)

# Generating a random list of numbers
random_list = datagen.generate_list(length=5, data_type=int, min_value=0, max_value=10)

# Generating a random list of strings
random_string_list = datagen.generate_list(length=3, data_type=str, min_length=3, max_length=5)
```

### Note: The release is scheduled for June 14, 2024.

This is just a brief overview of DataGen's capabilities. It offers a variety of functions for generating diverse random data, which can be used in various scenarios such as software testing, generating test data, and more.
