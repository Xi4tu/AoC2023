import re

def solution():
    with open("input.txt", "r") as f:
        total = 0
        for line in f:
            numbers_in_text = re.findall(r"\d", line)
            calibration_values = int(numbers_in_text[0]*2) if len(numbers_in_text) == 1 else int(numbers_in_text[0] + numbers_in_text[-1])
            total += calibration_values
    return total

if __name__ == '__main__':
    print(solution())