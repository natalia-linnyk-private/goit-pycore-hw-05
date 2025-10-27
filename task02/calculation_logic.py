import re

def generator_numbers(text):
    # Pattern to match numbers of type integer and float
    pattern_numbers = r'\b\d+\.?\d*\b'
    
    for match in re.finditer(pattern_numbers, text):
        try:
            yield float(match.group())
        except ValueError:
            continue

def sum_profit(text, generator_numbers):
    return sum(generator_numbers(text)) # Sum all numbers found in income text