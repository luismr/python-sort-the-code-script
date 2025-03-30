# Python Rank Array Script

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

A Python script that sorts alphabetic characters in a string.

## Project Structure

```
.
├── LICENSE.md
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    ├── sort_code.py
    └── test_sort_code.py
```

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone git@github.com:luismr/python-sort-the-code-script.git
cd python-sort-the-code-script
```

2. Create and activate a virtual environment:

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The script provides a function `sort_code` that takes a string input containing alphabetic characters and returns them sorted alphabetically.

```python
from src.sort_code import sort_code

# Example usage
result = sort_code("acbdfe")
print(result)  # Output: "abcdef"
```

### Input Parameters

- `s` (str): Input string containing up to 26 unique alphabetic characters
  - Optional: No
  - Default: None
  - Type: String
  - Constraints: Contains only alphabetic characters

### Return Value

- Returns a string with the same characters arranged alphabetically
- Type: String
- Length: Same as input string

## Testing

Run the test suite using:

```bash
python -m pytest src/test_sort_code.py -v
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. 