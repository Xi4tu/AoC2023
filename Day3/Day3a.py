import re
import string

def solution():
    with open("input.txt", "r") as f:
        lines = f.readlines() # Lista con las lineas
        total_lines = len(lines)
        special = string.punctuation.replace('.', '')
        valid_numbers = []
        for i, _ in enumerate(lines): # Recorrer lista con las líneas y con índice
            if i + 1 != total_lines:
                # Si no estamos en la última línea
                first_line = lines[i]
                down_line = lines[i + 1]
                up_line = None
                # Si además no estamos en la primera línea
                if i != 0:
                    up_line = lines[i - 1]
            else:
                # Estamos en la última línea
                up_line = lines[i - 1]
                first_line = lines[i]
                down_line = None
                
            numbers = re.finditer(r"(\d{1,})", first_line)
            for number in numbers:
                start = number.start()
                end = number.end()
                value = number.group()
                
                # Comprobar adjacente por los laterales                 
                if start - 1 != -1 and end < len(first_line):
                    if first_line[start - 1] in special or first_line[end] in special:
                        valid_numbers.append(int(value))
                        continue
                else:
                    # Compruebo izquierda solo
                    if end == len(first_line):
                        if first_line[start - 1] in special:
                            valid_numbers.append(int(value))
                            continue
                    # Compruebo derecha solo
                    elif start -1 < 0:
                        if first_line[end] in special:
                            valid_numbers.append(int(value))
                            continue
                    
                # Comprobar adjacente por arriba y por abajo
                for p in range(start - 1, end + 1):
                    if up_line and down_line:
                        if up_line[p] in special or down_line[p] in special:
                            valid_numbers.append(int(value))
                            break
                    
                    # Si hay contenido en la fila superior
                    elif up_line:
                        if up_line[p] in special:
                            valid_numbers.append(int(value))
                            break
                        
                    # Si hay contenido en la fila inferior
                    elif down_line:
                        if down_line[p] in special:
                            valid_numbers.append(int(value))
                            break
                    
    return sum(valid_numbers)                     
                        
                
if __name__ == '__main__':
    print(solution())