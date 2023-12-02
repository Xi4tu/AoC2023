from collections import defaultdict 
from functools import reduce

def solution():
        
    with open("input.txt", "r") as f:
        sum = 0
        
        for line in f:
            sets = line.split(':')[1].split(';')
            max_values = defaultdict(lambda: 0)
            
            for set in sets:
                subset = set.strip().split()
                
                for i, item in enumerate(subset):
                    if not item.isdigit():
                        color = item.replace(',', '')
                        if max_values[color] < int(subset[i - 1]):
                            max_values[color] = int(subset[i - 1])
                            
            sum += reduce(lambda x, y: x * y, max_values.values())

    return sum

if __name__ == '__main__':
    print(solution())