import re

def solution():
    d = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4e',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            text = line
            for k, v in d.items():
                text = text.replace(k, v)
            
            numbers_in_text = re.findall(r"\d", text)
            calibration_values = int(numbers_in_text[0]*2) if len(numbers_in_text) == 1 else int(numbers_in_text[0] + numbers_in_text[-1])
            total += calibration_values
            
    return total


if __name__ == '__main__':
    print(solution())