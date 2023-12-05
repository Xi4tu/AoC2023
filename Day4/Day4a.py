def solution():
    with open("input.txt", "r") as f:
        sum = 0
        
        for line in f:
            data = line.strip().split(':')[1].split('|')
            my_numbers = data[0].split()
            card = data[1].split()
            successes = -1
            
            for number in my_numbers:
                if number in card:
                    successes += 1
                    continue
            
            sum += 2 ** successes if successes != -1 else 0
                
    return sum

if __name__ == '__main__':
    print(solution())