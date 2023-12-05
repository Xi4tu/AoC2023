def solution():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        d = {i: 1 for i in range(1, len(lines) + 1)}
        n = 1
        
        for line in lines:
            data = line.strip().split(':')[1].split('|')
            my_numbers = data[0].split()
            card = data[1].split()
            successes = 0
            
            for number in my_numbers:
                if number in card:
                    successes += 1
                    
            if successes > 0:
                ini = n + 1
                fin = min(n + successes, len(lines))
                for i in range(ini, fin + 1):
                    d[i] += d[n] 
            n += 1
            
        return sum(d.values())

if __name__ == '__main__':
    print(solution())