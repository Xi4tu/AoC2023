import re

def solution():
    
    total_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    with open("input.txt", "r") as f:
        sum = 0
        
        for line in f:
            game_id = int(re.search(r"\d{1,}",line.split(':')[0]).group())
            sets = line.split(':')[1].split(';')
            isValid = True
            
            for set in sets:
                subset = set.strip().split()
                
                for i, item in enumerate(subset):
                    if not item.isdigit():
                        if total_cubes[item.replace(',', '')] < int(subset[i - 1]):
                            isValid = False
            
            sum += game_id if isValid else 0
    return sum

if __name__ == '__main__':
    print(solution())