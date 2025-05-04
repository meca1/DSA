"""
Python Basics - Variables and Data Types
"""

# Basic Types
number_variable = 42
string_variable = "Hello, Python!"
boolean_variable = True
none_variable = None

# Lists
number_list = [1, 2, 3, 4, 5]
string_list = ["a", "b", "c"]

# Tuples
tuple_example = ("age", 30)

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "is_active": True
}

# Set
unique_numbers = {1, 2, 3, 4, 5, 5}  # Duplicates are automatically removed

# Type Hints (Python 3.5+)
from typing import List, Dict, Union, Tuple, Optional

# Function with type hints
def add(a: int, b: int) -> int:
    return a + b

# Complex type hints
def process_data(items: List[str], config: Dict[str, Union[str, int]]) -> Tuple[int, Optional[str]]:
    # This is just a demonstration function
    return (len(items), config.get("message"))

# Usage examples
if __name__ == "__main__":
    print(f"Number: {number_variable}")
    print(f"String: {string_variable}")
    print(f"Person: {person['name']}, {person['age']} years old")
    print(f"Unique numbers: {unique_numbers}")
    print(f"2 + 3 = {add(2, 3)}")
    
    # Example with type hints
    result, message = process_data(
        ["item1", "item2"],
        {"message": "Success", "count": 2}
    )
    print(f"Processed {result} items. Message: {message}") 